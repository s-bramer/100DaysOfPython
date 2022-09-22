"""  
Sends an email if the ISS is within 5 degrees lat and long and it is night
"""
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians
import requests
import smtplib
import time


MY_LAT = 51.402560 # Your latitude
MY_LONG = -3.484190 # Your longitude
#MY_LAT = -47.1834 # Your latitude
#MY_LONG = 165.5801 # Your longitude

SENDER_EMAIL = "pickled.sprout.bay@gmail.com"
PASSWORD = "hrdeiaoysnreduss"
RECEIVER_EMAIL = "s.schultchen@gmx.com"
DISTANCE = 0
NEW_DISTANCE = 0
SPEED = 0

def is_dark():
    """returns true if it is dark"""
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise

def is_iss_near():
    """returns true if iss is within 5 degrees of your position"""
    global DISTANCE
    global NEW_DISTANCE
    global SPEED
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_long = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    #print (f"ISS currently on Lat: {iss_lat} Long: {iss_long}")

    NEW_DISTANCE = calculate_distance(iss_lat, iss_long)
    SPEED = round((NEW_DISTANCE-DISTANCE)/60,2)
    DISTANCE = NEW_DISTANCE

    return MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5

def calculate_distance(iss_lat, iss_long):
    """calculates distance between your position and the iss"""
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(MY_LAT)
    lon1 = radians(MY_LONG)
    lat2 = radians(iss_lat)
    lon2 = radians(iss_long)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return int(R * c)

def send_mail(email_text):
    """sends email 'look up' """
    email_subject = "Look up! eom"
    email_message = f"Subject: {email_subject}\n\n{email_text}"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.ehlo()
    connection.starttls() #make connection secure (Transport Layer Security)
    connection.ehlo()
    connection.login(user=SENDER_EMAIL, password=PASSWORD)

    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=email_message)
    connection.quit()

while True:
    time.sleep(60)
    if is_dark() and is_iss_near():
        print("Sending mail..")
        send_mail(f"The ISS is currently {DISTANCE}km away, moving at {SPEED}km/s..")
    print(f"Current distance {DISTANCE}km, moving at {SPEED}km/s.")
