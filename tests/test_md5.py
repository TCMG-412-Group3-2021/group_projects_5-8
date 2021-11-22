import requests

f = open('./hostName.txt', 'r')
hostName = f.readline()

def test_valid_input():
    prime_test = requests.get(f'http://{hostName}:80/md5/howdy').json()
    result= {'input': 'howdy', 'output': '0782efd61b7a6b02e602cc6a11673ec9'}
    assert prime_test == result

def test_invalid_input():
    prime_test = requests.get(f'http://{hostName}:80/md5//')
    assert prime_test.ok == False

def test_testing():
    prime_test = requests.get(f'http://{hostName}:80/md5/testing').json()
    result= {'input': 'testing', 'output': 'ae2b1fca515949e5d54fb22b8ed95575'}
    assert prime_test == result