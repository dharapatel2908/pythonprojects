import json


data = json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("Please check your word again. ")

word = input("Enter the word to find its meaning: ")
out=dictionary(word)
if type(out) == list:
    for item in out:
        print(item)
else:
    print(out)
