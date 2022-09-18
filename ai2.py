from lzma import FORMAT_ALONE
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from PIL import Image
import smtplib
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)


    
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'molly' in command:
                command = command.replace('molly', '')
                print(command)
    except:
        pass
    return command

def wishMe():
    talk('hey, wassup. i m molly. please tell me how may i help you')     

    


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('mollybot0307@gmail.com', 'wpecbfyeyimouitm')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'nitish'  : 'nitishm1803@gmail.com',
    'vicky'   : 'realtablestuff03@gmail.com',
    'rishita' : 'rishita2019@gmail.com',
    'star'    : 'jhasundarm@gmail.com',
    'ritesh'  : 'riteshmishra6143@gmail.com'
}


# def get_email_info():

#     # talk('To Whom you want to send email')
#     # name = take_command()
#     # receiver = email_list[name]
#     # print(receiver)
#     # talk('What is the subject of your email?')
#     # subject = take_command()
#     # talk('Tell me the text in your email')
#     # message = take_command()
#     # send_email(receiver, subject, message)
#     # talk('Your email is sent')
#     # talk('Do you want to send more email?')
#     # send_more = take_command()
#     # if 'yes' in send_more:
#     #     get_email_info()


# get_email_info()    

wishMe()

def run_molly():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a lot of work to do')
    elif 'are you single' in command:
        talk('I am in a relationship with my work')
    elif'i love you' in command:
        talk('i love you too but as a friend')
    elif 'do you know siri' in command:
        talk('she is a bitch. GO AND ASK THAT BITCH WHO SHE IS. AND NEVER EVER ASK ME ABOUT HER.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    
    
    elif 'hello' in command:
        talk("hello my name is molly. how can i help you?")    
    elif 'how are you' in command:
        talk("i m perfectly fine. what about you?")
    elif 'fine' in command:
        talk('great! how is your day going?')
    elif 'good' in command:
        talk('that is awesome. do you want me to do anything for you, like i can play some music for you or any video ')
    elif 'horrible' in command:    
        talk("okay. just relax and listen to some soothing music, it will make you feel good and you will be fine")
    elif 'bad' in command:    
        talk("okay. just relax and listen to some soothing music, it will make you feel good and you will be fine")
    elif 'dance' in command:
        talk("great. so let us have some music then")
        pywhatkit.playonyt('https://youtu.be/jbWrpmYVok4')
    elif 'f*** you' in command:
        talk("what did you just say you bitch, you son of a bitch. you better be aware or you will be fuck motherfucker")
        webbrowser.open("https://www.pexels.com/photo/woman-making-hand-sign-998850/")
    
    elif 'email' in command:
        talk('To Whom you want to send email')
        name = take_command()
        receiver = email_list[name]
        print(receiver)
        talk('What is the subject of your email?')
        subject = take_command()
        talk('Tell me the text in your email')
        message = take_command()
        send_email(receiver, subject, message)
        talk('Your email is sent successfully')  
    

        
    
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        webbrowser.open("google.com")  
    elif 'open erp' in command:
        webbrowser.open("http://mrei.icloudems.com/")      
    else:
        talk('Please say it again.')


while True:
    run_molly()