import os
from datetime import date
from datetime import datetime
from datetime import timedelta
import smtplib
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = "Y4MTNHMMXI9FTO4O"
STOCK_CHANGE = 0
EMAIL_PW = os.getenv("email_key")
SENDER_EMAIL = "pickled.sprout.bay@gmail.com"
RECEIVER_EMAIL = "s.schultchen@gmx.com"

def send_mail(email_text):
    """sends email"""
    email_subject = "Stock News!"
    email_message = f"Subject: {email_subject}\n\n{email_text}"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.ehlo()
    connection.starttls() #make connection secure (Transport Layer Security)
    connection.ehlo()
    connection.login(user=SENDER_EMAIL, password=EMAIL_PW)

    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=email_message.encode("utf-8"))
    connection.quit()


def stock_jump():
    """checks whether stock has increased/decreased by 5% between yesterday and the day before"""
    global STOCK_CHANGE 
    #get dates
    today = date.today()
    yesterday = str(date.today()- timedelta(days=1))
    db_yesterday = str(date.today()- timedelta(days=2))

    #access stock data
    alphavantage_endpoint = "https://www.alphavantage.co/query"
    stock_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }

    response = requests.get(alphavantage_endpoint, params=stock_parameters)
    response.raise_for_status()

    data = response.json()
        
    close_yesterday = float(data["Time Series (Daily)"][yesterday]['4. close'])
    close_db_yesterday = float(data["Time Series (Daily)"][db_yesterday]['4. close'])
    
    print(close_yesterday)
    print(close_db_yesterday)


    STOCK_CHANGE = round(((close_yesterday - close_db_yesterday)/close_yesterday)*100,2)
    if abs(STOCK_CHANGE) > 5:
        return True

def fetch_news():
    """gets all headlines for company"""
    NEWS_ENDPOINT = "https://newsdata.io/api/1/news"
    NEWS_API_KEY = "pub_11763ed2ffce288a5fa902526e5c3809bf1e0"
    news_parameters = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "language": "en",
    }
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    results = response.json()["results"]

    email_body = ""
    for article in range(len(results)):
        title = results[article]["title"]
        date = results[article]["pubDate"]
        email_body += "Title: " + str(title) + "\n"
    return email_body


if stock_jump():
    print("sending email")
    up_down = None
    if STOCK_CHANGE > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"
    news = f"TSLA: {up_down}{str(int(STOCK_CHANGE))}%\n\nHeadlines:\n"
    news += fetch_news()
    send_mail(news)
