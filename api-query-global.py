import requests
import pandas as pd
import tweepy
import json
import csv
def get_tweets(type_tweet="CaracolTV"):
    headers = {"Authorization": "Bearer {}".format('<your-bearer-token>')}
    url = "https://api.twitter.com/2/tweets/search/recent?query=from:"+f"{type_tweet}"
    print(url)
    response = requests.request("GET", url, headers=headers).json()
    df = pd.DataFrame(response)
    df.to_csv('Tweets_caracolRadio.csv')


def load_trends_world():
    headers = {"Authorization": "Bearer {}".format('<your-bearer-token>')}
    url = "https://api.twitter.com/1.1/trends/available.json"
    print(url)
    response = requests.request("GET", url, headers=headers).json()
    df = pd.DataFrame(response)
    df.to_csv('Tweets_Tendencias_Del_Mundo.csv')


def load_trends_closest(lat=4.598056,long=-74.075833):
    headers = {"Authorization": "Bearer {}".format('<your-bearer-token>')}
    url = "https://api.twitter.com/1.1/trends/closest.json?"+"lat="+f"{lat}"+"&"+"long="+f"{long}"
    print(url)
    response = requests.request("GET", url, headers=headers).json()
    df = pd.DataFrame(response)
    df.to_csv('Tweets_Tendencias_Mas_Cercanas.csv')    

def create_twitter_url():
    headers = {"Authorization": "Bearer {}".format('<your-bearer-token>')}
    handle = "CaracolTV"
    max_results = 100
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(
        mrf, q
    )
    print(url)
    response = requests.request("GET", url, headers=headers).json()
    df = pd.DataFrame(response['data'])
    df.to_csv('Analyze_the_sentiment_of_Tweets.csv')


def tendencias():
    headers = {"Authorization": "Bearer {}".format('<your-bearer-token>')}
    url = "https://api.twitter.com/1.1/trends/place.json?id=23424787"
    print(url)
    response = requests.request("GET", url, headers=headers).json()
    print(response)
    #df = pd.DataFrame(response)

    #df.to_json('Tweets_Tendencias_colombia.json')
    df = pd.read_json("Tweets_Tendencias_colombia.json")
    

    print(df)
    

    
if __name__ == '__main__':
    #a  = input('ingrese tweet a buscar:')

    create_twitter_url()
