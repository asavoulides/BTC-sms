import requests
from twilio.rest import Client
import locale
from datetime import datetime, timedelta
import json


# Set up the CoinMarketCap API

# Set up the News API
news_api_key = '3982781f3a644c7892bcdef212ff5b6f'



# Set the locale for the current system
locale.setlocale(locale.LC_ALL, '')

#Defining Variables

def current_price():
    # Retrieve the current Bitcoin price
    cmc_response = requests.get(cmc_url, headers=cmc_headers, params=cmc_params).json()
    return round(float(cmc_response['data']['BTC']['quote']['USD']['price']), 2)
    


def prev_change():
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    # Get yesterday's date
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')
    # Set the query parameters
    params = {'date': yesterday_str}
    # Send the API request
    response = requests.get(url, params=params)
    data = response.json()['data']
    prev_bitcoin_price = float(data['amount'])
    # Calculate percentage change from previous day
    price_change = current_price() - prev_bitcoin_price
    price_change_pct = (price_change / prev_bitcoin_price) * 100
    price_change_dir = '⬆️ ' if price_change >= 0 else '⬇️ '
    return  f'{price_change_dir} {abs(price_change_pct):.2f}'


def get_news():
    global news_api_key
    # Retrieve top Bitcoin news headline
    url = f"https://newsapi.org/v2/everything?q=bitcoin&language=en&sortBy=popularity&apiKey={news_api_key}"

    # send a request to the API
    response = requests.get(url)

    # parse the JSON response
    data = json.loads(response.text)

    # check if the response contains any articles
    if data["totalResults"] == 0:
        print("No articles found.")
        return 
    else:
        # print the headline and description of the first article
        article = data["articles"][0]
        title = article["title"]
        description = article["description"]
        source = article["url"]
    return f'{title} ⭐ {description}'



    # Add commas to Bitcoin price
    #bitcoin_price_str = locale.format_string('%.2f', bitcoin_price, grouping=True)

    client.messages.create(to=number, from_=twilio_number, body=msg)


def add_commas(number):
    # Convert number to a string
    number_string = str(number)

    # Split the string into integer and decimal parts
    if "." in number_string:
        integer_part, decimal_part = number_string.split(".")
    else:
        integer_part, decimal_part = number_string, ""

    # Reverse the integer part of the string
    reversed_integer_part = integer_part[::-1]

    # Create a list to store the result
    result = []

    # Loop through the reversed string, adding commas every three characters
    for i in range(0, len(reversed_integer_part), 3):
        result.append(reversed_integer_part[i:i+3])

    # Join the result list and reverse it to get the final string for the integer part
    final_integer_part = ",".join(result)[::-1]

    # Combine the integer and decimal parts back into a single string, if decimal part exists
    if decimal_part:
        final_string = final_integer_part + "." + decimal_part
    else:
        final_string = final_integer_part

    # Return the final string
    return final_string

#print(current_price())


