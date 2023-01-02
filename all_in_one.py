import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from tkinter import *
from PIL import ImageTk, Image

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voices',voices[0].id)

class Assitant():
    def speak(self,audio):
        engine.say(audio)
        engine.runAndWait()

    def greet(self):
        hour = datetime.datetime.now().hour
        if hour >=0 and hour<12:
            self.speak("Good morning sir How may I help you") 
        elif hour >=12 and hour<18:
            self.speak("Good afternon sir How may I help you") 
        else:
            self.speak("Good evening sir How may I help you") 
        
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

    def start(self):
        self.greet()
        query = self.takeCommand().lower()

        if 'wikipedia' in query:
            self.speak("Searching Wikipeadia .. ")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            print(results)
            self.speak(results)

        elif 'how are you' in query:
            self.speak("Glad to hear that I am good what about you")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
            
        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            exit()

        else:
            self.speak('Command is not recognize exiting program')
            exit

win = Tk()
a = Assitant()
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("voice.jpeg"))
on = Button(win,text="Start", command=a.start).place(relx=0.475,rely=0.27)

# Create an object of tkinter ImageTk

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

win.mainloop()