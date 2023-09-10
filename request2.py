import requests

def response2():
    response = requests.get ( "http://numbersapi.com/random/math" )
    return response.text