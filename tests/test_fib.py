import requests

f = open('./hostName.txt', 'r')
hostName = f.readline()

# valid test with valid input
def test_valid_input():
    fib_test = requests.get(f'http://{hostName}:80/fibonacci/5').json()
    result = {'input': 5, 'output': [0, 1, 1, 2, 3, 5]}
    assert fib_test == result

# valid test with invalid input
def test_invalid_input():
    fib_test = requests.get(f'http://{hostName}:80/fibonacci/five')
    assert fib_test.ok == False

def test_0():
    fib_test = requests.get(f'http://{hostName}:80/fibonacci/0').json()
    result = { 'input': 0, 'output': [0] }
    assert fib_test == result

def test_100():
    fib_test = requests.get(f'http://{hostName}:80/fibonacci/100').json()
    result = { 
        'input': 100,
        'output': [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    }
    assert fib_test == result