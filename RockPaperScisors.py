import random
import time

n = ["rock","paper","scisors","rock","paper","scisors"]

#Functions

#1 == scisors
#2 == paper
#3 == rock

def comparepaper():
  
  if comp == 1 and playerinput == "paper":
    print("Lost to computer! Computer's input : Scisors. Player's input : Paper")
  elif comp == 2 and playerinput == "paper":
    print("Draw! Computer's input : Paper. Player's input : Paper")
  else:
    print("Won! Computer's input : rock. Player's input : Paper")

def comparerock():
  
  if comp == 1 and playerinput == "rock":
    print("Won! Computer's input : Scisors. Player's input : Rock")
  elif comp == 2 and playerinput == "paper":
    print("Lost to computer! Computer's input : Paper. Player's input : Rock")
  else:
    print("Draw! Computer's input : Rock. Player's input : Rock")

def comparescisors():
  
  if comp == 1 and playerinput == "scisors":
    print("Draw! Computer's input : Scisors. Player's input : Scisors")
  elif comp == 2 and playerinput == "paper":
    print("Won! Computer's input : Paper. Player's input : Scisors")
  else:
    print("Lost to computer! Computer's input : Rock. Player's input : Scisors")

#Define variables

comp = n[random.randint(0,5)]

name = input("What's your name?   ")
time.sleep(1)
print("Hello, " + name)

playerinput = input("rock, paper or scisors?   ")

#print(playerinput)

#print("Computer chose " + comp)

time.sleep(1.5)

#if statements

if playerinput == "paper":
  comparepaper()
elif playerinput == "rock":
  comparerock()
elif playerinput == "scisors":
  comparescisors()
else:
  print("not a valid answer! please try again.")

#1 == scisors
#2 == paper
#3 == rock
