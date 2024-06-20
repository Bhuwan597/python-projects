import pyttsx3,os
import speech_recognition as sr
import datetime
import cv2,random
import wikipedia
from requests import get
import webbrowser
import pywhatkit as kit
import pyautogui
import time,math
from pynput.keyboard import Key, Controller
import smtplib 
import sys
import playsound,winsound
from yaspin import yaspin
import os
import requests
from bs4 import BeautifulSoup
import psutil
import speedtest  
from plyer import notification
from email.message import EmailMessage


keyboard = Controller()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def desktop_notify(title,message):
    notification.notify(title=title,message=message,timeout = 10, app_icon = 'bell.ico')

# text to speech
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
# Alarm Beep 
def playbeep():
    playsound.playsound('alarm.wav', True)

# Weather Forecast
def weather_forecast():
    search = 'Temperature in Dhangadhi'
    url = f'https://google.com/search?q={search}'
    r= requests.get(url)
    data = BeautifulSoup(r.text,'html.parser')
    temp = data.find('div',class_='BNeawe').text

    url = 'https://www.wunderground.com/forecast/np/dhangadhi'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    weather = soup.find_all('span', class_ = 'wx-value')
    return temp,search,weather[1].text
def speed_test():
    st = speedtest.Speedtest()
    st = speedtest.Speedtest()
    upload_speed = math.ceil(st.upload()/(1000000)) 
    download_speed =  math.ceil(st.download()/(1000000)) 
    ping = math.ceil(st.results.ping) 
    return upload_speed,download_speed,ping

# Send Email
def sendEmail(subject,to,content):
    msg = EmailMessage()
    msg['subject'] = subject
    msg['From'] = 'v1acharya34@gmail.com'
    msg['To'] = to
    msg.set_content(content)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('v1acharya34@gmail.com','ogfirexfmdsdysng')
    server.send_message(msg)
    server.quit()
    speak(f'Email has been sent to {to}')
    desktop_notify('Email sent successfully', f'Email has been sent to {to}')

def first_command():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print('********* Listening *********')
        audio = r.listen(source)
        print('********* Recognizing ********')
        try:
            say = r.recognize_google(audio, language='en-in')
            print(f'You said: {say}')
            return say
        except:
            return ''

# Take command from the user(voice to text)
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        with yaspin(text="Listening to your voice . . . . . .", color="green") as spinner:
            # playsound.playsound('mic.wav',False)
            winsound.Beep(700,500)
            r.pause_threshold=1
            audio = r.listen(source,timeout=2,phrase_time_limit=5)
            spinner.ok('✅')

    try:
        with yaspin(text="Recognizing your voice . . . . . .", color="green") as spinner:
            winsound.Beep(700,500)
            query = r.recognize_google(audio,language='en-in')
            print(f'\nYou said: {query}')
            spinner.ok("✅ ")

    except:
        speak("Sorry sir, I didn't hear you properly")
        print('😢😌😢🙉')
        spinner.fail("❌ ")
        return ''
    return query

# Wish you good morning/afternoon
def wish():
    hour = int(datetime.datetime.now().hour)
    current_time = datetime.datetime.now().strftime('%H:%M %p')
    if hour > 0 and hour <12:
        speak(f'Good morning sir, Its {current_time}')
        print('🥰🥰🥰🥰🥰')
    elif hour >12 and hour <18:
        speak(f'Good afternoon sir , Its {current_time}')
        print('🥰🥰🥰🥰🥰')
    else:
        speak(f'Good evening sir, Its {current_time}')
        print(' 🥰🥰🥰🥰🥰')
    speak('How may i assist you?')
    print('🤷‍♂️🤷‍♀️🤷‍♂️🤷‍♀️🤷‍♂️')
def main_function():
            wish()
            while True:
                try:
                    query = take_command().lower()
                except:
                    query = take_command().lower()
                    
                # Logic building for tasks
                if 'notepad' in query:
                    notepad_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\\Notepad"
                    os.startfile(notepad_path)
                elif 'command prompt' in query:
                    command_prompt_path = r"C:\Users\v1ach\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt"
                    os.startfile(command_prompt_path)
                elif 'camera' in query:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret,img = cap.read()
                        cv2.imshow('webcam',img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                elif 'music' in query:
                    music_dir = "D:\Songs"
                    songs = os.listdir(music_dir)
                    # rd = random.choice(songs)
                    for song in songs:
                        if song.endswith('.mp4') or song.endswith('.mp3'):
                            os.startfile(os.path.join(music_dir,song))
                        break
                
                elif 'ip address' in query:
                    with yaspin(text="Finding your ip address", color="green") as spinner:
                        try:
                            ip = get('https://api.ipify.org').text
                            speak(f"Your ip address is {ip}")
                            desktop_notify('Ip Address', f"Your ip address is {ip}")
                            spinner.ok('✅')
                        except:
                            speak('Some error occured while finding your ip address.')
                            spinner.fail('❌')

                elif 'wikipedia' in query:
                    with yaspin(text="Wikipedia", color="green") as spinner:
                        speak('Searching on wikipedia')
                        query = query.replace('wikipedia','')
                        try:
                            results = wikipedia.summary(query,sentences = 2)
                            speak(f'\nAccording to wikipedia, {results}')
                            spinner.ok('✅')
                        except:
                            speak('Please sir, try using simple keywords')
                            spinner.ok('❌')

                elif 'internet speed' in query or 'network speed' in query or 'wifi speed' in query:
                    speak('Please hang in there for few seconds, I am checking your internet speed.')
                    with yaspin(text="Checking your internet speed", color="green") as spinner:
                        try:
                            upload_speed,download_speed,ping = speed_test()
                            spinner.ok('✅')
                            speak(f"Your internet have upload speed of {upload_speed} megabites per second, download speed of {download_speed} megabites per second and latency of {ping}")
                            desktop_notify('Internet Speed',f"Your internet have upload speed of {upload_speed} megabites per second, download speed of {download_speed} megabites per second and latency of {ping}")
                        except:
                            spinner.fail('❌')
                            speak('Sorry sir, there was a problem on checking your internet speed.')

                elif 'open youtube' in query:
                    speak('What you want to play on youtube?')
                    yt = take_command().lower()
                    kit.playonyt(yt)

                elif 'open facebook' in query:
                    webbrowser.open("https://facebook.com",new = 2)

                elif 'open instagram' in query:
                    webbrowser.open("https://instagram.com",new = 2)

                elif 'open twitter' in query:
                    webbrowser.open("https://twitter.com",new = 2)

                elif 'google' in query:
                    speak('Sir, What should i search on google?')
                    cm = take_command().lower()
                    webbrowser.open(f'{cm}')
                elif 'weather' in query or 'temperature' in query:
                    temp,search,weather = weather_forecast()
                    speak(f'Current {search} is {temp} and weather throughout the day will be {weather}')
                    weather_forecast()  
                    desktop_notify('Weather Report',f'Current {search} is {temp} and weather throughout the day will be {weather}')
                elif 'whatsapp' in query:
                    speak('Type the number you want to send message')
                    number = '+977'+ input('Type phone number: ')
                    speak('What message would you like to send?')
                    while True:
                        message = take_command().lower()
                        if message != '':
                            kit.sendwhatmsg_instantly(number,message,tab_close=True)
                            time.sleep(4)
                            pyautogui.click()
                            time.sleep(1)
                            break
                        else:
                            speak('Try saying the message again')

                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    speak(f"Message sent to {number}!")
                    desktop_notify('Whatsapp Message',f"Message sent to {number}!")

                elif 'battery percentage' in query or 'charging' in query:
                    is_charging = psutil.sensors_battery().power_plugged
                    battery_percentage = psutil.sensors_battery().percent 
                    if is_charging:
                        speak(f'Sir, our system have {battery_percentage} % power and the system is plugged in.')
                    elif battery_percentage >= 80:
                        speak(f'Sir, our system have {battery_percentage} % power and we have enough power to continue our work.')
                    elif battery_percentage >= 50:
                        speak(f'Sir, our system have {battery_percentage} % power and we should connect our system to charging point.')
                    elif battery_percentage >= 25:
                        speak(f'Sir, our system have {battery_percentage} % power and we have very lower power, maybe we should connect to charger as soon as possible.')
                    else:
                        speak(f'Sir, our system have {battery_percentage} % power and we have very lower power so system is  going to shutdown in few minutes. ')
                    desktop_notify('Battery Status', f'Battery: {battery_percentage}%')
                    

                elif 'email' in query or 'gmail' in query:
                    try:
                        speak('To whom i  send an email message?')
                        to = input('Type email')
                        speak('What will be the subject of this email?')
                        subject = take_command().lower()
                        speak('What should i send as email message?')
                        content = take_command().lower()
                        sendEmail(subject,to,content)
                    except Exception as e:
                        print(e)
                elif 'alarm' in query:
                    speak('Please, provide the time you want to set alarm')
                    try:
                            day,hour,min = input('day/hour/min : ').split('/')
                            speak('Wait, Setting alarm for you')
                            day_from_now = int(day) - int(datetime.datetime.now().day)
                            d = int(day_from_now)+ (int(hour)-int(datetime.datetime.now().hour))/24 + (int(min) - int(datetime.datetime.now().strftime('%M')))/(24*60)
                            alarm = datetime.timedelta(days=d)
                            full_time = datetime.datetime.now() + alarm
                            compare_alarm_time = full_time.strftime('%d/%H/%M')
                            time.sleep(1)
                            speak('Alarm Set successfully')
                            while True:
                                minute_left = (full_time.timestamp() - datetime.datetime.now().timestamp())//60
                                if str(compare_alarm_time) == datetime.datetime.now().strftime('%d/%H/%M'):
                                    count = 0
                                    desktop_notify('Alarm', f'Wake up Bhuwan its {compare_alarm_time}' )
                                    while True:
                                        speak('Wake up Bhuwan')
                                        count+=1
                                        if count == 6:
                                            break
                                        playbeep()
                                        time.sleep(1)
                                    break
                                else:
                                    # speak(f'{int(minute_left)} minutes left for alarm')
                                    time.sleep(60 - int(datetime.datetime.now().strftime('%S')))
                    except:
                        time.sleep(1)
                        speak('Sorry something went wrong while setting up alarm')

                elif 'where am i' in query or 'location' in query or 'what is my location' in query or 'where' in query:
                    speak('Wait sir, Let me find your location')
                    with yaspin(text="Finding your location", color="green") as spinner:
                        try:
                            ip_address = get('https://api.ipify.org').text
                            url='https://get.geojs.io/v1/ip/geo/'+ ip_address + '.json'
                            time.sleep(1)
                            geo_array = get(url).json()
                            city = geo_array['city']
                            country = geo_array['country']
                            spinner.ok('📍')
                            speak(f'Your current location is in country {country} and {city} city.')
                            desktop_notify('Current Location',f'Your current location is in country {country} and {city} city.')
                        except:
                            speak('Sorry sir, there was a problem on finding your location.')
                            spinner.fail('❌')

                elif 'exit' in query or 'quit' in query:
                    playsound.playsound('terminate.mp3', False)
                    speak('Thanks for using me. Have a good day sir.')
                    sys.exit()
                elif 'sleep' in query or query == '' or 'no' in query or 'No' in query:
                    playsound.playsound('terminate.mp3', False)
                    speak("Okay sir, I'm going to sleep now. You can call me any time.")
                    break                   
                else:
                    with yaspin(text="Error", color="red") as spinner:
                        speak("\nSorry sir, i didn't get you")
                        spinner.fail('❌')
                time.sleep(2)
                speak('\nSir do you have any other tasks?')
                print(' ✌ ✌ ✌ ✌ ✌')
if __name__=='__main__':
    while True:
        permission = first_command().lower()
        if 'quit' in permission or 'exit' in permission or 'bye' in permission:
            playsound.playsound('terminate.mp3', False)
            speak('Thanks for using me. Have a good day sir.')
            sys.exit()
        elif 'hey leo' in permission or 'wake up leo' in permission or 'leo wake up' in permission or 'leo' in permission:
            main_function()

    