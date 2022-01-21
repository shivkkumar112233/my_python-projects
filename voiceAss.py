from tkinter import *
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()
#to make the assistant to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to greet the user
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning buddy") 
        window.update()
        speak("Good Morning buddy!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon buddy!")
        window.update()
        speak("Good Afternoon buddy!")
    else:
        var.set("Good Evening buddy")
        window.update()
        speak("Good Evening buddy!")
    speak("Myself ven! How may I help you buddy") 
#to take commands from the user and to recognize
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold =1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query
#to start the assistant based on the commands from user
def play():
    btn2['state'] = 'disabled'
   
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        #to exit
        if 'exit' in query:
            var.set("Bye buddy")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            
            window.update()
            speak("Bye sir")
            break
        #to open wikipedia
        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
                break
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                    break
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')
        #to open youtube
        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")
            break
        elif 'open instagram' in query:
            var.set('opening instagram')
            window.update()
            speak('opening instagram')
            webbrowser.open("https://www.instagram.com/")
            break
        elif 'open facebook' in query:
            var.set('opening facebook')
            window.update()
            speak('opening facebook')
            webbrowser.open("https://www.facebook.com/")
            break
        
        elif 'open twitter' in query:
            var.set('opening ')
            window.update()
            speak('opening twitter')
            webbrowser.open("https://twitter.com/")
            break
        #to open google   
        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")
            break
        #to play music
        elif ('play music' in query) or ('change music' in query):
            var.set('Here are your favorites')
            speak('Here are your favorites')
            window.update()
            webbrowser.open("https://www.youtube.com/results?search_query=telugu+songs")
            break
        #to display time
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("buddy the time is %s" % strtime)
            window.update()
            speak("buddy the time is %s" %strtime)
            
        #to display date
        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("buddy today's date is %s" %strdate)
            window.update()
            speak("buddy today's date is %s" %strdate) 
        
        #to greet the assistant
        elif 'thank you' in query:
            var.set("Welcome buddy")
            window.update()
            speak("Welcome buddy")
        #to ask assistant what tasks it can perform
        elif 'can you do for me' in query:
            var.set('I can do multiple tasks for you buddy. tell me whatever you want to perform buddy')
            window.update()
            speak('I can do multiple tasks for you buddy. tell me whatever you want to perform buddy')
        #to known how world the assistant is
        elif ' how old are you' in query:
            var.set("I am a little baby buddy")
            window.update()
            speak("I am a little baby buddy")
        #to known name of the assistant
        elif ' your name' in query:
            var.set("Myself ven Sir")
            window.update()
            speak('myself ven sir')
        #to known creator of assistant
        elif 'who created you' in query:
            var.set('My Creator is Mr. batch1')
            window.update()
            speak('My Creator is Mr. batch1')
        #to greet the assistant
        elif 'say hello' in query:
            var.set('Hello Everyone! My self ven')
            window.update()
            speak('Hello Everyone! My self ven')
        #to open chrome
        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Program Files \\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
            btn1['state'] = 'normal'
            window.update()
            break
        #to exit if the assistant does not recognize the commands
        else:
            speak("sorry buddy")
            speak("i am unable to process")
            speak("bye buddy") 
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            window.update()
            break
    btn1.configure(bg = '#5C85FB')
    btn2['state']='normal'
    btn1['state']='normal'
    var1.set("welcome")
    var.set("hi")
   # window.update()
#to update the window
def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('welcome')

label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('hi')
label1.pack()

frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('ven')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)


btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()