import requests

f = open('./hostName.txt', 'r')
hostName = f.readline()

def test_valid_input():
    slack_test = requests.get(f'http://{hostName}:80/slack-alert/howdy').json()
    result= {'input': 'howdy', 'output': True, 'message': 'howdy'} 
    assert slack_test== result

def test_string_input():
    slack_test = requests.get(f'http://{hostName}:80/slack-alert/This was sent from a testing suite!').json()
    result= {'input': 'This was sent from a testing suite!', 'output': True, 'message': 'This was sent from a testing suite!'} 
    assert slack_test== result

def test_invalid_input():
    slack_test = requests.get(f'http://{hostName}:80/slack-alert//')
    assert slack_test.ok == False