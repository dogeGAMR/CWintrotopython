#!/usr/bin/python3
print("Content-type: text/html \n")

import magic_wand
import random

####### H O M E W O R K ############
#
# 	Homework 2: Implement the logic of a basic chatbot. 
# 				- Create a function with one parameter message
# 				- Use an if-elif statements to return the reply to message
# 				- For instance, if message is  "how are you",
# 				- return  "I am fine"
# 				- Add at-least 5 replies to the message in this function
# 
#####################################
messages =["Hello","How are you","What is your name?","What do you do?","What language are you written in?"]
random = random.randint(0,4)
def chat(message) :
    if message == "Hello" :
        return "Hi"
    elif message == "How are you" :
        return "I am doing well."
    elif message == "What is your name?" :
        return "I am Ziggy"
    elif message == "What do you do?" :
        return "I exist to chat with you."
    elif message == "What language are you written in?" :
        return "I am written in python."
    else :
        return "I don't know that one"
    
output = chat(messages[random])
prompt = messages[random]
print("Input: \n")
print(prompt,"\n")
print("Output: \n")
print(output)

