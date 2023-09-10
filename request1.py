import requests

def response1():
    response = requests.get ( "http://numbersapi.com/random/trivia" )

    return response.text