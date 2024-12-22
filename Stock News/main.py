import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "9VZJUO2YVWNZPPPD"
NEWS_API_KEY = "aa94d4ee50af4597921cb587f79c9ec7"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_SID = "AC6a0c65997bcfa4e26136950e2cb2e479"
TWILIO_TOKEN = "12df427c6b7ceb87d6483af62bc0908c"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = yesterdays_data["4. close"]
print(yesterdays_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterdays_closing_price) - float(day_before_yesterday_closing_price)
print(difference)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "🔽"

diff_percentage = round(difference / float(yesterdays_closing_price)) * 100
print(diff_percentage)

if abs(diff_percentage) > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    article = news_response.json()["articles"]

    three_articles = article[:3]
    print(three_articles)

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline:{article['title']}. \nBrief: {article['description']}" for
        article in
        three_articles]

    client = Client(TWILIO_SID, TWILIO_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(body=article, from_="+14847465164", to="+919037390947")
