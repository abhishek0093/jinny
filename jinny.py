'''
pitch and voice
text and voice both
'''
from urllib import response
import pyttsx3
import datetime
import speech_recognition as sR
import wikipedia
import webbrowser
import subprocess
import smtplib
import requests
import pyjokes

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)
engine.setProperty('rate', 120)
engine.setProperty('volume', 0.8)
asst_name = 'Jinny'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12 ):
        speak("Good Morning Dear! Wish You a good day ahead")
    elif(hour>=12 and hour < 18):
        speak("A Very Good Afternoon Dear!")
    else:
        speak("Good Evening! Enjoy the pleasant weather Outside, Dear")
    speak(f"I am {asst_name}")

def userInput():
    '''
    Takes audio Input from user's microphone using speech recognistion module
    '''
    input = sR.Recognizer()
    with sR.Microphone() as source:
        print("Listening to you Dear ........")
        input.pause_threshold = 0.5
        input.energy_threshold = 400
        audio = input.listen(source)
    try:
        print("Processing your query...........")
        query = input.recognize_google(audio)
        print(f"User Said : {query}\n")
    except sR.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "nR"  
    except Exception as e:
        print("Please Say It again.......")
        return "failed"
    return query

def sendEmail(emailAddr, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    file = open('/home/abhishek/Downloads/python/CWH/test.txt','r')
    server.login('abhishek.mi072@gmail.com', file.read())
    server.sendmail('abhishek.mi072@gmail.com', emailAddr, content)


if __name__ == "__main__":
    greetMe()
    while True:
        speak("How may I help you?")
        query = userInput().lower()
        if('wikipedia' in query):
           speak('Fetching results from wikipedia, please wait..')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)
        elif('open application' in query):
            try:
                app_dict = {1:"google-chrome", 2:"firefox", 3:"code"}
                print(app_dict)
                speak("Please say the number code of application to be opened from the list on screen")
                app_num = int(userInput())
                subprocess.call(app_dict[app_num])
            except Exception as e:
                print(e)
                speak("Some Error faced while opening the application. Did you said it correctly?")
        elif('open' in query):
            query = query.replace('open ', "")
            webbrowser.open(query)
        elif('weather' in query):
            speak("Please say your city")
            city = userInput().title()
            API_key = 'd70d331752b4678a563a13cd3ab7fcb0'
            response = requests.get("https://api.openweathermap.org/data/2.5/weather?"+"q= "+city+"&units=metric&appid="+API_key)
            if(response.status_code == 200):
                res = response.json()
                temp = res['main']['temp']
                temp_min = res['main']['temp_min']
                humidity = res['main']['humidity']
                wind_speed = res['wind']['speed']
                report = res['weather']
                speak(f"Showing results for {city}, a city located in Country with code {res['sys']['country']}")
                print(f"{city}, {res['sys']['country']} ----------------------------")
                print(f"Current temperature: {temp} °C")
                print(f"Wind Speed: {wind_speed} m/s")
                print(f"Humidity: {humidity} %")
                print(f"Weather Report: {report[0]['description']}")
                speak(f"Current temperature is {temp} degree celsius. Wind speed is {wind_speed} meter per second")
                speak(f"Humidity is {humidity} %")
                speak("In Short weather is "+str(report[0]['description']))
            else:
                speak("Faced Some Error in fetching weather updates")
        elif('time' in query):
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print("It is : ", time)
            speak(f"It is {time}")
        elif('change assistant name' in query):
            speak("I am Very Excited to get a new name, what you would like to call me?")
            asst_name = userInput().title()
            speak(f"Great! Now I am your {asst_name}")
        elif('news' in query):
            try:

                API_key = '2dfd2e372ee84e97b34dde6f93d760ea'
                response = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey="+API_key)
                if(response.status_code == 200):
                    res =  response.json()
                    speak("How Many articles you wanna read")
                    num_articles = int(userInput())
                    while(num_articles > res['totalResults']):
                        speak("Sorry I can't fetch these many articles, please choose a smaller number.")
                        speak("How Many articles you wanna read")
                        num_articles = int(userInput())
                    for i in range(num_articles):
                        name = res['articles'][i]['source']['name']
                        print(f"News Headline {i+1} is from {name}\n")
                        speak(f"News Headline {i+1} is from {name}")
                        news_des = res['articles'][i]['description']
                        print(news_des+"\n")
                        print("URL : "+res['articles'][i]['url'])
                        speak(news_des)
                else:
                    speak("Some error faced in fetching the news")
            except Exception as e:
                print(e)
                speak("Some Error occured as shown in screen")

        elif("send email" in query):
            try:
                speak("Please say email address of the recipient")
                emailAddr = userInput().lower().replace(" ", "")
                print(emailAddr)
                speak("Check the email address on the screen , If it is correct say ok, otherwise say something else")
                status = userInput().lower()
                while(status != 'ok'):
                    speak("please say the email address again")
                    emailAddr = userInput().lower().replace(" ", "")
                    print(emailAddr)
                    speak("Check the email address on the screen , If it is correct say ok, otherwise say something else")
                    status = userInput().lower()
                speak("What will be the subject of Email?")
                subject = userInput().title()
                speak("Please say body of your mail")
                body = userInput()
                message = 'Subject: {}\n\n{}'.format(subject, body)
                sendEmail(emailAddr, message)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                print("Some Error tackled while sending Email. Please Fix me")
                speak("Error faced while sending email")

        elif('quit' in query or 'over' in query):
            speak("Thankyou for using me! Good Bye")
            break;
        elif('joke' in query):
            joke = pyjokes.get_joke()
            print(joke);
            speak(joke+" Hahahah")
        else:
            speak("Please say something that I can process")
        speak("Thank You!")

else:
    print ("Executed when imported")