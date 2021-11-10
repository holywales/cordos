import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import ctypes
import winshell
import subprocess
import pyjokes
import requests
import json
import wolframalpha
import time
from selenium import webdriver
from time import sleep
from geopy.geocoders import Nominatim
import wikipediaapi
import glob
import yfinance as yf
import eyed3
eyed3.log.setLevel("ERROR")
import re
import socket
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# import pygame
from PIL import Image
from urllib.request import urlopen
import os.path

# import for music player
import tkinter as tk
from tkinter import *
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from tkinter import filedialog
from pathlib import Path
import os.path
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
from tkvideo import tkvideo
import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
import threading
from threading import Thread



# import long_responses as long

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')           #getting details of current voice
rate=engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[0].id)     #changing index, changes voices. 0 for male
# engine.setProperty('voice', voices[1].id)     #changing index, changes voices. 1 for female



root = Tk()




# Create text widget and specify size.
T = Text(root, height = 5, width = 52)

root.title('Cody ')
root.iconbitmap('./images/aurora.ico')
root.geometry("600x650")

# create Master frame
master_frame = Frame(root)
master_frame.pack(pady=20)

# VOICE ASSISTANT CODE
# Create text display
text_box = Listbox(master_frame, width=80)
text_box.grid(row=0, column=0, padx=10)

# create the input
e = Entry(master_frame, width=50)
e.grid(row=1,column=0, pady=30)



# speech recognizer
def rec_audio():
    data = input("You:" )
    return data

# send the input to text display
def mySend():
    # myLabel = Label(master_frame)
    txt = e.get()
    # Insert The texx.
    john = "You : "+ txt
    text_box.insert(tk.END, john)
    text = "cody "+ txt
    call(text)




# display text and speak audio
def text_audio(texts):
    john = "Cody: " + texts 
    text_box.insert(tk.END, john)
    e.delete(0,END)


# display text and speak audio

# get today's date
def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."

# Assistant processing information
def res():
    res = ["One Sec...","Processing...","Thinking..."][random.randrange(3)]
    text_audio(res)

def powerdown():
    exit()

global Name
Name = "User"
       

# check if wake word is in sentence
def call(text):

    global Name
    speak = " "
    action_call = "cody"
    text = text.lower()
    print(Name)
    # check if action word is in sentence
    def there_exists(terms):  
        for term in terms:  
            if term in text:  
                return True

    # check if other action doesn't exist
    def there_not_exists(terms):  
        for term in terms:  
            if term not in text:  
                return True  


    try:
        if action_call in text:
            
            
            # first action
            if there_exists(['hello']):
                speak = "Hello"
        
            # second action
            if there_exists(['good morning','good afternoon','good evening','good day','good night']):
                hour = int(datetime.datetime.now().hour)
                if hour>= 0 and hour<12:
                    speak = "Good Morning."

                elif hour>= 12 and hour<18:
                    speak = "Good Afternoon."

                elif hour>=18 and hour<24:
                    speak = "Good Evening." 

            elif there_exists(['what is the time','what time is it']):
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."
         
            elif there_exists(['who are you', 'define yourself','what is your name']):
                if Name == "User":
                    speak = " My name is Cody. What's your name?"

                else:
                    speak = "My name is Cody, your virtual assistant. Nice to meet you, "+ Name                    



            elif there_exists(['why do you exist', 'why did you come']):    
                speak = speak + "I am here to make your experience wonderful"

            elif there_exists(['my name is','i am']) and there_not_exists(['play','youtube','search']):  
                
                if "my name is" in text:  
                    
                    person_name = text.split("is")[-1].strip()  
                    # person_obj.setName(person_name.title()) # remember name in person object 
                    
                    Name = person_name.title()
                    speak = "Okay, i will remember that, " + person_name.title()  
                elif "i am" in text: 
                    person_name = text.split("am")[-1].strip()  
                    # person_obj.setName(person_name.title()) # remember name in person object 

                    Name = person_name.title()  
                    speak = "Okay, i will remember that, " + person_name.title()  
                                    
            # third action
            elif there_exists(['today date','what month','today\'s date']):
                get_today = today_date()
                speak = get_today        

            elif there_exists(['open']) and there_not_exists(['notes','note']):
                res()
                if "chrome" in text.lower():
                    speak = "Opening Google Chrome"
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )

                elif "word" in text.lower():
                    speak = "Opening Microsoft Word"
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                    )

                elif "excel" in text.lower():
                    speak = "Opening Microsoft Excel"
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
                    )

                elif "visual studio code" in text.lower():
                    speak = "Opening Visual Studio Code"
                    os.startfile(
                        r"C:\Users\Lamour\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    )

                elif "youtube" in text.lower():
                    speak =  "Opening Youtube\n"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = "Opening Google\n"
                    webbrowser.open("https://google.com/")

                elif "stackoverflow" in text.lower():
                    speak = "Opening StackOverFlow"
                    webbrowser.open("https://stackoverflow.com/")

                else:
                    speak = "Application not available"

            elif there_exists(['play']):
                if "play music" in text or "play song" in text:  
                    speak = "Apple music or spotify. I think you should use the internet"

            elif there_exists(['who am i']) and there_not_exists(['play','youtube','search']):
                uname = Name
                if uname != "User":
                   speak = "Your name is "+ Name 
                else:
                    speak = "You must probably be a human. What is your name?"                   

            elif there_exists(['power down','exit','quit']):
                speak = "Powering down."
                # files = glob.glob('/sound/*')
                # for f in files:
                #     os.remove(f)
                powerdown() 

        text_audio(speak) 
    # except Exception as e:

    #     print(e)  
    except :
        text_audio("I couldn't get that. You can try something else")  



    


# create send button
myButton =Button(master_frame, text=" Send ", command=mySend)
myButton.grid(row=2,column=0)



# MP3PLAYER CODE
# definitions for music player


# Song directory
music_dir = r"C:\Users\Lamour\Music"



video_name = './chatbotVideo/chatbotNormal50.mp4' 
# create label
video_label = Label(master_frame)
# video_label.grid(row=3, columnspan=2)
video_label.grid(rowspan=3)
# read video to display on label
player = tkvideo(video_name, video_label, loop=1, size = (550, 350))
player.play()



tk.mainloop()


  