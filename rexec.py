######
# The purpose of this program is to download emails to xxx.xxx@gmail.com and
# interpret them as instructions to be executed on machines at WSP
######
# Author: Rob Mengert
# Date: 3/6/19
######

import imapclient, pyzmail, openpyxl, paramiko, contactmyself
# contactmyself contains custom functions to login the gmail imap server

# Set some variables used to perform some validation later
subjectMatch = 'xxxxxxxx'
sender = 'xxxxxxx@gmail.com'

# Initalize variables
uid_match = {}

# Login to Gmail IMAP server and fetch the unread messages
imapObj = contactmyself.imaplogin()
imapObj.select_folder('Inbox', readonly=True)
unreadMessages = imapObj.search('UNSEEN')
rawMessages = imapObj.fetch(unreadMessages, ['BODY[]', 'FLAGS'])

# Get the password cell location for the xlsx file
pwFile = open('password_line', 'r')
pwLoc = pwFile.read()
pwFile.close()

# Open password xlsx file and grab password
wb = openpyxl.load_workbook('xxxxxxx.xlsx')
sheet = wb.active
sheetPw = sheet[pwLoc].value

# Wrap the password_line to the next cell
cellRow = int(''.join(i for i in pwLoc if i.isdigit()))
newCellRow = cellRow + 1
sheet = wb.active

if sheet['A' + str(newCellRow)].value is None:
    # check if the cell A'newCellRow' is blank and roll back to the second row if it is
    newCellRow = 2

# Update the password cell
newCell = 'A' + str(newCellRow)
pwFile = open('password_line', 'w')
pwFile.write(newCell)

for uid, message_data in rawMessages.items():
    # Loop through all of the unread messages

    message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])
    if message.get_subject().startswith(subjectMatch) and message.get_address('from')[1] == sender:
        # Verify the sender and that the subject starts with subjectMatch
        uid_match[uid] = message.get_subject().split(':')[1]
        # create dictionary entries with the UIDs as the key and the password as the value.  Mails in this dictionary
        # have the proper subject match and came from a 'verified' sender.


for uid, emailPw in uid_match.items():
    # loop through the matched emails

    if sheetPw != emailPw:
        # verify the password passed in the email matches the password from the sheet
        print('Invalid password, exiting.')
        exit(1)

    # extract hostname and instructions to be run from the content of the mail, the text_part.get_payload()
    # function out of the pyzmail library looks promising.

    message = pyzmail.PyzMessage.factory(rawMessages[uid][b'BODY[]'])
    # get the raw message in the message variable
    payload = message.text_part.get_payload().decode()
    # get just the payload of the message into the payload variable
    payloadList = payload.split('\r\n')
    # get the lines of the message into list elements by splitting on the '\r\n' spacing that gets added to mails
    payloadList = [x for x in payloadList if x]
    # remove any blank list elements using a list comprehension
    if len(payloadList) != 2:
        # Exit if there were not exactly two arguments passed
        print("Improper amount of arguments passed, exiting")
        exit(1)

    for emailLine in payloadList:
        # for each list element, check if one is a host and the other a command and exit if they're not
        argument = emailLine.split(':')[0].lower()
        if argument == 'host':
            host = emailLine.split(':')[1]
        elif argument == 'command':
            command = emailLine.split(':')[1]
        else:
            print('Invalid argument passed, exiting')
            exit(1)

    # Actually execute the command and capture it's output to reply to the sender
    client = paramiko.SSHClient()
    sshKey = paramiko.RSAKey.from_private_key_file('/home/user/.ssh/id_rsa')
    client.connect(hostname = host, username = 'user', pkey = sshKey)
    stdin, stdout, stderr = client.exec_command(command)

    # TODO: Reply to mail with the output from the command

# disconnect from the current IMAP session
imapObj.logout()

# Reconnect to the IMAP session without readonly mode turned on and fetch the mails that were executed so that
# they're marked as read. Use the uid_match dictionary to pull this off.

imapObj = contactmyself.imaplogin()
imapObj.select_folder('Inbox')

for uid in uid_match.keys():
    imapObj.remove_flags([uid], 'UNSEEN')
    imapObj.add_flags([uid], '\\Seen')
