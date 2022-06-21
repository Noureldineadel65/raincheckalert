import requests
API_KEY = "dd91a9e6a83c49a6f37752ea71c27844"
import smtplib
import datetime as dt
def get_user_location():
    response = requests.get("https://ipinfo.io/json")
    response.raise_for_status()
    LAT, LNG = response.json()["loc"].split(",")
    return {
        "LAT": float(LAT),
        "LNG": float(LNG)
    }

USER_LOC = get_user_location()

def get_weather_details():
    parameters = {
        "lat": "33.565109",
        "lon": "73.016914",
        "appid": API_KEY,
        "exclude": "current,minutely,daily"
    }
    API = "https://api.openweathermap.org/data/2.5/onecall"
    response = requests.get(API, params=parameters)
    response.raise_for_status()
    data = response.json()
    return data
weather_details = get_weather_details()
def raining(weather_data):
    hourly_list = weather_data["hourly"][:11]
    gonna_rain = False
    for i in hourly_list:
        id = i["weather"][0]["id"]
        if id < 700:
            gonna_rain = True
    return gonna_rain
current_hour = dt.datetime.now().hour
if raining(weather_details) and current_hour >= 7:
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login("jzblbot@outlook.com", "JEZEBELISABOT112004")
        smtp.sendmail(from_addr="jzblbot@outlook.com", to_addrs="noureldine.adel22@gmail.com",
                      msg=f"Subject:NOUR GRAB A JACKET!\n\nIts gonna be raining today!\n\nCaptured at: {dt.datetime.now()}\n")