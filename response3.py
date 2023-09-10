import requests



def response3(b):
    response = requests.get ( "http://numbersapi.com/" + b + "/trivia" )
    return response.text