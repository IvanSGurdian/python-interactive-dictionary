import json
from difflib import get_close_matches

# Loads JSON data & converts into dict python object
data = json.load(open('data.json'))


def search_word(key):
    key = key.lower() #sets all characters to lowercase
    if key in data: 
        definition = data[key]
        return definition
    elif key.title() in data: # looks for capitalized words like state names (e.g. texas = Texas)
        return data[key.title()]
    elif key.upper() in data: # looks for uppercase words like acronyms (e.g. USA, NATO, etc )
        return data[key.upper()]
    elif len(get_close_matches(key, data.keys())) > 0:
        newKey = get_close_matches(key, data.keys())[0]  #looks for similar words in case of type errors and returns first match
        response = input("Did you mean '%s' instead? (y/n)" % newKey)
        if response.lower() == 'y':
            return data[newKey]
        else:
            return "The word doesn't exist"
    else:
        return "The word doesn't exist"


word = input('Enter a word to search: ')
output = search_word(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
