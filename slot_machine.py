#!/usr/bin/python3
print("Content-type: text/html \n")

import magic_wand
import random

####### E X E R C I S E ############
# 
# Exercise 1: Get three random numbers for our slot machine.
#
# Exercise 2: Give a reward if all numbers are the same.
#
# Exercise 3: Use logical operators to check slot items.
#
# Exercise 4: Show fruits or any other item instead of numbers.
#
# Bonus: If the value in item is divisible by 2, give more reward.
#
# Homework 1: Use 6 items in slot machine instead of 3.
# 			  - Get three additional random numbers between 0 and 3
#  			  - Store the result in variables, and print them along with other items.
#  			  - Using the and operator, add additional conditions to check if all numbers are same.
#  			  - Similarly, add additional conditions to the elif statement using the or operator.
#
######################################
debug = 0
debug1 = 0

if debug == 1 :
    debug1 = 0
elif debug == 2 :
    debug1 = 1
else :
    debug1 = 3

slot1 = random.randint(0,debug1)
slot2 = random.randint(0,debug1)
slot3 = random.randint(0,debug1)
slot4 = random.randint(0,debug1)
slot5 = random.randint(0,debug1)
slot6 = random.randint(0,debug1)
slot7 = random.randint(0,debug1)
slot8 = random.randint(0,debug1)
slot9 = random.randint(0,3)
emoji = ["&#127818;","&#127815;","&#127826;","&#129373;"]
print(f"""
{emoji[slot1]} : {emoji[slot2]} : {emoji[slot3]}
{emoji[slot4]} : {emoji[slot5]} : {emoji[slot6]}
{emoji[slot7]} : {emoji[slot8]} : {emoji[slot9]}
""")
print(f"""
{slot1} : {slot2} : {slot3}
{slot4} : {slot5} : {slot6}
{slot7} : {slot8} : {slot9}
""")
def slots(s1,s2,s3,s4,s5,s6,s7,s8,s9) :

    if slot1 == slot2 and slot2 == slot3 and slot3 == slot4 and slot4 == slot5 and slot5 == slot6 and slot6 == slot7 and slot7 == slot8 and slot8 == slot9 :
        return "hit the jackpot and won a diamond token"
    elif slot1 == slot5 and slot5 == slot9 and slot3 == slot5 and slot5 == slot7 :
        return "got a <b>X<b> and won two gold tokens"
    elif slot1 == slot5 and slot5 == slot9 :
        return "got a diagonal and won a platium token"
    elif (slot1 == slot4 and slot4 == slot7) or (slot2 == slot5 and slot5 == slot8) or (slot3 == slot6 and slot6 == slot9) or (slot1 == slot2 and slot2 == slot3) or (slot4 == slot5 and slot5 == slot6) or (slot7 == slot8 and slot8 == slot9) :
        return "got a 3 in a row and won a gold token"
    elif slot1 == slot2 or slot2 == slot3 or slot4 == slot5 or slot5 == slot6 or slot7 == slot8 or slot8 == slot9 or slot1 == slot4 or slot4 == slot7 or slot2 == slot5 or slot5 == slot8 or slot3 == slot6 or slot6 == slot9 :
        return "got a 2 in a row and won a silver coin"
    else:
        return "got no matches and won nothing"
    
    
reward = slots(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9)

print(f"You {reward}.")
