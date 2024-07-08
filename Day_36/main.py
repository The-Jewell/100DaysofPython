import requests
from twilio.rest import Client
import api_keys as keys

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



# Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": keys.STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


# Find the difference between the daily stock prices
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round(difference / float(yesterday_closing_price) * 100)
print(diff_percent)

# If percentage is greater than 5 then get news articles for company name
if abs(diff_percent) > 5:
    new_params = {
        "apiKey": keys.NEW_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = news_response.json()["articles"]

    # list that contains the first 3 articles
    three_articles = articles[:3]

    # new list of the first 3 articles headline and description
    formatted_article_list = [(f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
                               f"Headline: {article['title']}. \nBrief: {article['description']}")
                              for article in three_articles]

    # Send each article as a separate message via Twilio.
    client = Client(keys.TWILIO_SID, keys.TWILIO_AUTH)
    for article in formatted_article_list:
        message = client.messages.create(
            body=article,
            from_="+18556259469",
            to="2293159376"
        )
else:
    pass
