import pyttsx3
import win32com
import os
import sys
  
# initialisation   #pip install pypiwin32 # pip install pyttsx3 #pip install pywin32
engine = pyttsx3.init() 
  
# testing 
engine.say("ご清聴ありがとうございました。") 
engine.runAndWait() 
