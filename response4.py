import requests

def response4(b):
    response = requests.get ( "http://numbersapi.com/" + b + "/math" )
    return response.text