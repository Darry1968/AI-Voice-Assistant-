# AI-Voice-Assistant-

Our voice assistant is a customizable virtual assistant that uses natural language processing to understand and respond to voice commands. It can perform a variety of tasks, such as greeting users, searching the web, opening apps, and playing music, as well as many other tasks if desired. This project was developed using Python and it's various libraries.

## How this works?

In order to use this voice assistant project, which was built using Python, you will need to install some modules. To install any module use
```
pip install [module_name]
```
These are some required modules.

```python
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from tkinter import *
from PIL import ImageTk, Image
```

Now let's understand the use of each module.<br/><br/>
**1. pyttsx3 -** 'pyttsx3' is a text-to-speech conversion library in Python. It uses different speech engines based on your operating system:

nsss - NSSpeechSynthesizer on Mac OS X<br/>
sapi5 - SAPI5 on Windows<br/>
espeak - eSpeak on any platform<br/>
auto - will try to use the above three in that order<br/>

It can be used as shown below in your python code
```
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voices',voices[0].id)
```
We create a function to get response from our system, like we created in our class Assistant
```
def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()
```
For more information you can read the documentation of 'pyttsx3'.

**2. datetime -** The 'datetime' module is a built-in Python library that provides classes for working with dates and times. I used this module for greeting purpose it can be used for remainders also. The greet function is as shown below,
```
def greet(self):
        hour = datetime.datetime.now().hour
        if hour >=0 and hour<12:
            self.speak("Good morning sir How may I help you") 
        elif hour >=12 and hour<18:
            self.speak("Good afternon sir How may I help you") 
        else:
            self.speak("Good evening sir How may I help you")
```
You can find more information and examples in the datetime module documentation.

**3. speech_recognition -** The speech_recognition module is a library for performing speech recognition in Python. It allows you to recognize speech from audio files or microphone input in real-time.<br/>

```
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
```
You can then use the Recognizer instance to perform speech recognition on audio files or microphone input. And recognize speech from an audio file. We have used for exception handling for handling any error occurs while recognizing the voice. The whole function as shown below.
```
 def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recoginzing .. ")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said : {query}\n")
        except Exception as e:
            print("Say that again")
            return "None"
        return query
```
You will find more information in the documentation of this module.

**4. wikipedia -** As name suggests it is used for searching purposes. The wikipedia module is a Python wrapper for the Wikipedia API. It allows you to search Wikipedia and retrieve the results programmatically in your Python code. You can then use it in your Python code by importing it and calling the summary() function to get the result of the your search result:
```
if 'wikipedia' in query:
    self.speak("Searching Wikipeadia .. ")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences = 2)
    print(results)
    self.speak(results)
```
You can find more information and examples in the wikipedia module documentation.

**5. webbrowser -** The webbrowser module is a built-in Python library that provides functions for opening web pages in your default web browser.

```
elif 'open youtube' in query:
    webbrowser.open("youtube.com")

elif 'open google' in query:
    webbrowser.open("google.com")

elif 'open stack overflow' in query:
    webbrowser.open("stackoverflow.com")
            
elif 'open spotify' in query:
    webbrowser.open("spotify.com")
```
This part of code shows the uses of webbrowser module. If there is something like "open youtube" in query so the open() function of this module will open youtube in web browser.
You can find more information and examples in the webbrowser module documentation.

**6. os -** The os module is a built-in Python library for interacting with the operating system. It provides functions for working with files, directories, and processes, as well as miscellaneous utility functions. I used this module for playing music there are many other use cases of this module you can use as per your desire.

```
elif 'play music' in query:
    music_dir = 'D:\\Music'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[0]))
    exit()
```
Note: You have to add your own music dictionary then only this will work. Read the documentation for more explaination and the examples.

**7. tkinter -** tkinter is a Python module for creating graphical user interfaces (GUIs). It is a thin object-oriented layer on top of the Tcl/Tk GUI toolkit, which is written in C. You can create the main window for your application and add widgets (elements such as buttons, labels, and text fields) to it. tkinter provides a wide range of widgets and layout management options, such as Frame, Label, Entry, Listbox, Menu, and Canvas. You can use these widgets to build complex user interfaces by arranging them in a layout using pack, grid, or place.

**8. PIL -** The Python Imaging Library (PIL) is a library for working with image files in Python. It allows you to read and write a wide range of image file formats, such as BMP, JPG, PNG, GIF, and TIFF.<br/>
By combining these two module i created an interface to interact with user when he wants to start this module. This part you can see in this part of code
```
win = Tk()
a = Assitant()
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("voice.jpeg"))
on = Button(win,text="Start", command=a.start).place(relx=0.475,rely=0.27)

# Create a Label Widget to display the Image
label = Label(frame, image = img)
label.pack()

win.mainloop()
```
Remember that you have to adjust the position of that start button if coordination of that button are messed up XD.

There are some drawbacks of this project which are listed below-
1. Requires internet connection. 
2. Mediocre sound quality.
3. Background noise interface.
4. Could be improved if provided with more!

*Thanks for your support. Happy Reading ;)*
