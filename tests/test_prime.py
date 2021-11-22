import requests

f = open('./hostName.txt', 'r')
hostName = f.readline()

# valid test with valid input
def test_valid_input():
    fib_test = requests.get(f'http://{hostName}:80/is-prime/5').json()
    result = {'input': 5, 'output': True}
    assert fib_test == result

# valid test with invalid input
def test_invalid_input():
    fib_test = requests.get(f'http://{hostName}:80/is-prime/five')
    assert fib_test.ok == False

def test_2():
    fib_test = requests.get(f'http://{hostName}:80/is-prime/2').json()
    result = { 'input': 2, 'output': True }
    assert fib_test == result

def test_100():
    fib_test = requests.get(f'http://{hostName}:80/is-prime/100').json()
    result = { 'input': 100, 'output': False }
    assert fib_test == result