import tweepy
import requests
import json
import time

API = "YNDmqZ7KIQfz05mJ5UH2iUW96"
api_key_secret = "inPMlkfKG1bAu3jEAMQmPPQKVTnK72NX8eEXsbJnZWAkp656ga"
bearertoken = "AAAAAAAAAAAAAAAAAAAAALXtawEAAAAA0Iue9sAXNWk1HVqXKWU9zpFWz5A%3DP8PCB5VTt8ud4OopsI57SqL3Adz2vAWl7gLqFmZDOpnY7zn1HN"
accesstoken = "1509571461266419715-sMZB14yh7DAcV94AnhUJZ9jwjvpnwp"
access_token_secret = "CvmUMbXvS4CKj3nFTch5Ciigdvwvm3qccbCdCf2KlayRx"

auth_handler = tweepy.OAuthHandler(consumer_key=API, consumer_secret=api_key_secret)
auth_handler.set_access_token(accesstoken, access_token_secret)

api = tweepy.API(auth_handler, wait_on_rate_limit=True)

switch = 1
while switch == 1:
    crypto = requests.get(
        'https://api.coingecko.com/api/v3/simple/price?ids=the-sandbox%2Cdecentraland%2C&vs_currencies=inr%2C%2C'
    )
    price_crypto_inr = crypto.json()

    SAND = str(price_crypto_inr['the-sandbox']['inr'])
    MANA = str(price_crypto_inr['decentraland']['inr'])
    #tweet = "📉BTC: ₹" + bitcoin  +"\n" + "📉ADA: ₹" + cardano +"\n" + "📈SOL: ₹" + solana +"\n" + "💸ETH: ₹" + ethereum 
    tweet2 = "⌛SAND: ₹" + SAND +"\n" + "🧝‍♂️MANA: ₹" + MANA
    #api.update_status(tweet)
    api.update_status(tweet2)
    #print(tweet)
    print(tweet2)
    time.sleep(10*60*60)
    print("Tweeted")
