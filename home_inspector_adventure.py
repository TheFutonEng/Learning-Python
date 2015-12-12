# This is a program that is basically
# a text adventure game of the glamorous
# life of a home inspector!
######
# Date: 11/30/2015
# Author: Rob Mengert
######

from sys import exit
import random
import numpy as np

#items_to_check = [[0 for x in range(1)] for y in range(1)]
items_to_check = [[],[]]

def dining_room():
    room = "dining room"    
    print "This is the %s, what do you want to do?" % room
    
    while True:
        print "1) Go to kitchen"
        print "2) Go to living room"
        print "3) Check for broken stuff"
        print "*) F this noise, I'm out"
        choice = raw_input('> ')

        if choice == '1':
            kitchen()
        elif choice == '2':
            living_room()
        elif choice == '3':
            broken_stuff(room)
        elif choice == '*':
            quit() 
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room
              
    

def kitchen():
    room = "kitchen"
    print "This is the %s, what do you want to do" % room
    
    while True: 
        print "1) Go to living room"
        print "1) Go to dining room"
        print "3) Check for broken stuff"
        print "*) F this noise, I'm out"
        choice = raw_input('> ')
    
        if choice == '1':
            living_room()
        elif choice == '2':
            dining_room()
        elif choice == '3':
            broken_stuff(room)
        elif choice == '*':
            quit() 
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room
              

def living_room():
    room = "living room"
    print "This is the %s, what do you want to do" % room
   
    while True:
        print "1) Go to the kitchen"
        print "2) Go to the dining room"
        print "3) Go to the basement"
        print "4) Go to the hallway"
        print "5) Go to the garage"
        print "6) Check for broken stuff"
        print "*) F this noise, I'm out"
        choice = raw_input('> ')

        if choice == '1':
            kitchen()
        elif choice == '2':
            dining_room()
        elif choice == '3':
            basement()
        elif choice == '4':
            hallway()
        elif choice == '5':
            garage()
        elif choice == '6':
            broken_stuff(room)
        elif choice == '*':
            quit() 
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room
 

def hallway():
    room = "hallway"    
    print "This is the hallway, nothing wrong here, where to?"
    
    while True:
        print "1) Bedroom 1"
        print "2) Bedroom 2"
        print "3) Bathroom"
        print "*) F this noise, I'm out"
        choice = raw_input('> ')

        if choice == "1":
            bedroom1()
        elif choice == "2":
            bedroom2()
        elif choice == "3":
            bathroom()
        elif choice == "*":
            quit()
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room
        

def basement():
    room = "basement"
    print "This is the %s, what do you want to do" % room
    
    while True:
        print "1) Go back up to the living room"
        print "2) Check for broken stuff"
        print "*) F this noise, I'm out"
        choice = raw_input('> ')

        if choice == "1":
            break
        elif choice == "2":
            broken_stuff(room)
        elif choice == "*":
            quit()
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room
            


def bedroom1():
    room = "bedroom1"
    print "This is the %s, what do you want to do" % room

    while True:
        print "1) Go back into the hallway"
        print "2) Check for broken stuff"
        print "*) F this noise, I'm out"
        choice = raw_input('> ')

        if choice == "1":
            break
        elif choice == "2":
            broken_stuff(room)
        elif choice == "*":
            quit()
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room

    

def bedroom2():
    room = "bedroom2"
    print "This is the %s, what do you want to do" % room
    
    while True:
        print "1) Go back into the hallway"
        print "2) Check for broken stuff"
        print "*) F this noise, I'm out"
        choice = raw_input('> ')

        if choice == '1':
            break
        elif choice == '2':
            broken_stuff(room)
        elif choice == '*':
            quit()
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room

def bathroom():
    room = "bathroom"
    print "This is the %s, what do you want to do" % room

    while True:
        print "1) Go back into the hallway"
        print "2) Check for broken stuff"
        print "*) F this noise, I'm out"
        choice = raw_input('> ')

        if choice == '1':
            break
        elif choice == '2':
            broken_stuff(room)
        elif choice == '*':
            quit()
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room

def garage():
    room = "garage"
    print "This is the %s, what do you want to do" % room

    while True:
        print "1) Go back outside"
        print "2) Go inside the house"
        print "3) Check for broken stuff"
        print "*) F this noise, I'm out"
        choice = raw_input('> ')
        
        if choice == "1":
            start()
        elif choice == "2":
            living_room()
        elif choice == "3":
            broken_stuff(room)
        elif choice == "*":
            quit()
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room


def foyer():
    room = "foyer"
    print "This is the foyer, nothing wrong in here. Where to?"
    
    while True:
        print "1) Dining Room"
        print "*) F this noise, I'm out"
        choice = raw_input('> ' )

        if choice == "1":
            dining_room()
        elif choice == '*':
            quit() 
        else:
            print "That wasn't an option (idiot), you're still in the %s, where to?" % room
        

def quit():
    print "This home inspector stuff is driving me to drink, meet you at the bar"
    print "Oh yeah, here's what's wrong with the place"
    #i=0
    #int(i)
    #for row in items_to_check:
    #    print items_to_check[[i],[i]]
    exit(0)

def start():
    print "You approach the house that needs an inspection"
    print "There is a front door or a garage door"
    print "Which do you open?"

    choice = raw_input('> ')
    
    if "garage" in choice:
        garage()
    elif "front" in choice:
        foyer()
    else:
        print "That wasn't a way to get inside the house!"

def broken_stuff(room):
    #print "recording all of the broken stuff in a room here"
    broken_items = []
    broken_items.append("electrical")
    broken_items.append("plumbing")
    broken_items.append("water damage")
    broken_items.append("busted door")
    broken_items.append("broken light")
    broken_items.append("bow chicka wow wow residue")
    broken_items.append("ghost")
    broken_items.append("entrance to another dimension")
    broken_items.append("being rejected by the house")
    
    broken_item = broken_items[random.randint(0,8)]
    #items_to_check.append([[room]broken_items[random.randint(0,8)]])
    items_to_check[0].append(room)
    items_to_check[1].append(broken_item)
    
    print "Well, it looks like the %s has %s problems" % (room, broken_item)

start()
