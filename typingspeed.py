from time import *
import random as r
import pyttsx3
from math import floor
test = [
    'A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.',
    'Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.',
    'JavaScript is a scripting language that enables you to create dynamically updating content, control multimedia, animate images.'
]
engine = pyttsx3.init('sapi5')
def speak(tospeak):
    print(tospeak)
    engine.say(tospeak)
    engine.runAndWait()

speak('Typing speed challenge begins\n')

def mistake(paragraph,userinput):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != userinput[i]:
                error+=1
        except:
            error = error+1
    accuracy = 100 - ((error/len(paragraph))*100)
    return error,accuracy

random_item = r.choice(test)
print(random_item+'\n')
time1 = time()
userinput = input('\nEnter:\n')
time2 = time()

def speed(time1, time2, userinput):
    time_difference = time2 - time1
    round_time = round(time_difference,2)
    total_words_typed = len(userinput.split(" "))
    speed = (total_words_typed/round_time)*60
    return round(speed)

def conclusion(errors,accuracy):
    totalspeed = speed(time1,time2,userinput)
    speak(f"The speed of your typing was {totalspeed} words per minute. You made {errors} errors with accuracy of {floor(accuracy)}%")

errors,accuracy = mistake(random_item,userinput)

conclusion(errors,accuracy)
