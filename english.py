import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        w = get_close_matches(w, data.keys(), n=9)[0]
        print("Did you mean "+w+" instead?")
        choice = input("Y/N? Enter Y if yes and N if no\n")
        if choice == "Y":
            return data[w]
        elif choice == "N":
            return "The word doesn't exist.Please double check it."
        else:
            return "We didn't understand your query"
    else:
        return "The word doesn't exist.Please double check it."


word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
