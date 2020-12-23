import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    w = get_close_matches(w, data.keys(), n=9)[0]
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist.Please double check it."


word = input("Enter word: ")
print(translate(word))
