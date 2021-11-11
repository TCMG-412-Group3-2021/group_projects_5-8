
import requests

def test_fib_test():
    fib_test = requests.get('http://10.228.181.245:80//fibonacci/5').json()
    result= {'input': 5, 'output': [0, 1, 1, 2, 3, 5]}
    assert fib_test== result

def test_prime_test():
    prime_test = requests.get('http://10.228.181.245:80//is-prime/3').json()
    result= {'input': 3, 'output': True}
    assert prime_test== result

def test_factorial_test():
    factorial_test = requests.get('http://10.228.181.245:80//factorial/9').json()
    result= {"input":9,"output":362880}
    assert factorial_test== result

def test_md5_test():
    md5_test = requests.get('http://10.228.181.245:80//md5/hello').json()
    result= {"input":"hello","output":"5d41402abc4b2a76b9719d911017c592"}
    assert md5_test== result

#Need to fix line 27     
# def test_slack_test():
#     slack_test = requests.get('http://10.228.181.245:80///slack-alert/howdy').json()
#     result= {} 
#     assert slack_test== result