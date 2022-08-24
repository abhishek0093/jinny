# Introduction : 
Tired out of typing and clicking down the things? what about putting your voice to some work? 

Jinny is a personal assistant that can do do following things for you:
* Sending Email
* Weather Report of any city
* Wikipedia summary
* Fetch latest news
* Open Applications 
* Cracking Jokes
* Reading aloud date and time. 

It uses espeak module to speak out the things, uses google's speech_recognition module to listen to the user and pyttsx module to convert it to text. 

## Sending Email 
User speaks out the email address of the recipient, the subject of the email, the body of the email and that's all . Your email will be sent. 
The project uses Smtplib.SMTP to send the email.

## Weather Report 
The user will speak out his city name , and using the openweather API the jinny will read out the current weather in your locality. 

## Wikipedia Summary 
The jinny will search your query over the wikipedia, and will read out the summary for you using the wikipedia module. 

## Open Applications 
Using the system call, the jinny will open the desired application on your laptop for you. 

## News
Are you also a news Keeda? The jinny can help you fetch the latest news around Your country (currently set to india) using the newsapi.org's api. 

## Jokes
using the pyjokes module, jinny can make you laugh too. 

## Date and Time
Simply using datetime module . 

#Future Improvements 
* Currently user will need to necessarliy speak some particular word in the sentence to process his/her query. 
* Making it more interactive. 
