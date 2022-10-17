#1 /usr/bin/python3

import requests
from profanity_check import predict

def get_word():
    random_word = ""

    response = requests.get("https://random-word-api.herokuapp.com/word")
    random_word = response.json()[0]
    return random_word, get_definition(random_word)

def get_definition(word):
    definitions = []

    response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    response_json = response.json()

    try:
        for i in range(len(response_json[0]["meanings"])):
            for j in range(len(response_json[0]["meanings"][i]["definitions"])):
                profanity = predict([f'{ response_json[0]["meanings"][i]["definitions"][j]["definition"]}'])
                if (profanity[0] == 1) {
                    get_word()
                } else {
                    definitions.append(f'({response_json[0]["meanings"][i]["partOfSpeech"]}) ' + response_json[0]["meanings"][i]["definitions"][j]["definition"])
                }
    except KeyError:
        get_word()
    
    return definitions