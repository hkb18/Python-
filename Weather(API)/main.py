import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "AC6a0c65997bcfa4e26136950e2cb2e479"
auth_token = "12df427c6b7ceb87d6483af62bc0908c"
OWN_Endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "5dd054ee39cc84c7575a55200c1d0e37"
# MY_LAT = 10.179900000000002
# MY_LONG = 76.33100927116489
MY_LAT = 28.504810
MY_LONG = 77.069520

weather_param = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}

will_rain = False
response = requests.get(OWN_Endpoint, params=weather_param)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    prxy_client = TwilioHttpClient()
    prxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=prxy_client)
    message = client.messages.create(
        body="It's going to rain today. Rememeber to bring an UMBRELLA ☂☔",
        from_='+14847465164',
        to='+919037390947'
    )

    print(message.status)
