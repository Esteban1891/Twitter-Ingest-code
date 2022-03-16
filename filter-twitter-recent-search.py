import requests
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = '<your_bearer_token>'

def create_url():
    type_tweet="CaracolTV"
    return "https://api.twitter.com/2/tweets/search/recent?tweet.fields=context_annotations&max_results=100&query=to:"+f"{type_tweet}"
    #return "https://api.twitter.com/2/tweets/sample/stream"
    #return "https://api.twitter.com/1.1/trends/place.json?id=23424787"
    #return "https://api.twitter.com/2/tweets/search/recent?tweet.fields=context_annotations&max_results=100&query=camping(nature%20OR%20%22outdoor%20actvities%22)"
    #return "https://api.twitter.com/2/tweets/search/stream?tweet.fields=created_at&expansions=author_id&user.fields=created_at"

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    print(response.status_code)
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


def main():
    url = create_url()
    timeout = 0
    while True:
        connect_to_endpoint(url)
        timeout += 1


if __name__ == "__main__":
    main()
