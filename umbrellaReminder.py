import schedule
import smtplib
import requests
from bs4 import BeautifulSoup

def umbrellaReminder():
    city = "State College" # Creating a url with the city name.
    url = "https://www.google.com/search?q=" + "weather" + city 
    html = requests.get(url).content

    soup = BeautifulSoup(html,'html.parser')   # Pass the retrieved HTML document into Soup which will return a string stripped of  HTML tags and metadata. 
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text 
    time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 

    # formatting data 
    sky = time_sky.split('\n')[1]

# sending an email with an umbrella reminder. 
    if sky == "Rainy" or sky == "Rain And Snow" or sky == "Showers" or sky == "Haze" or sky == "Cloudy": 
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

        # Starting a transport layer security to encyrpt all SMTP commands.
        smtp_object.starttls()

        # Pass in gmail account credentials to login.
        smtp_object.login("Your Email", "Password")
        subject = "REMINDER TO GRAB UMBRELLA!"
        body = f"Grab an umbrella before leaving the house!\
        Weather condition for today is {sky} and temperature is\
        {temperature} in {city}."

        # Saving the message to the variable below message.
        message = f"Subject:{subject}\n\n{body}\n\nRegards,\nAum's Umbrella Reminder".encode( 
            'utf-8')

        # Use the sendmail() instance to send your message.
        smtp_object.sendmail("From Email Address",
                            "To Email Address", message)

        # Ending the session
        smtp_object.quit() 
        print("Email Sent!")

# Sends an email everyday at 6 AM. 
schedule.every().day.at("06:00").do(umbrellaReminder)   
while True: 
    schedule.run_pending()
