import urllib.request
import json


def get_joke(url, category):
    api = url + category
    req = urllib.request.Request(
        url=api,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webURL = urllib.request.urlopen(req)
    data = webURL.read()
    joke = json.loads(data)
    return joke['value']


all_categories = ["animal", "career", "celebrity", "fashion",
                  "food", "history", "money", "movie", "music",
                  "science", "sport", "travel"]

category = "animal"
url = "https://api.chucknorris.io/jokes/random?category="

joke = get_joke(url, category)
print(joke)

