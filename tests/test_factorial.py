import requests

f = open('./hostName.txt', 'r')
hostName = f.readline()

def test_valid_input():
    prime_test = requests.get(f'http://{hostName}:80/factorial/0').json()
    result= {'input': 0, 'output': 1}
    assert prime_test == result

def test_invalid_input():
    prime_test = requests.get(f'http://{hostName}:80/factorial/seven')
    assert prime_test.ok == False

def test_10():
    prime_test = requests.get(f'http://{hostName}:80/factorial/10').json()
    result= {'input': 10, 'output': 3628800}
    assert prime_test == result

def test_1():
    prime_test = requests.get(f'http://{hostName}:80/factorial/1').json()
    result= {'input': 1, 'output': 1}
    assert prime_test == result