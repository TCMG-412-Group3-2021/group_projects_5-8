import requests

f = open('./hostName.txt', 'r')
hostName = f.readline()

# POST
def test_valid_post():
    payload = { 'key': 'testKey', 'value': 'testValue' }
    keyval_test = requests.post(f'http://{hostName}:80/keyval', json=payload).json()
    result= {'key': 'testKey', 'value': 'testValue', 'command': 'key is testKey and the value is testValue', 'result': True, 'error': '' } 
    assert keyval_test == result

def test_invalid_post():
    payload = { 'key': 'testKey', 'value': 'testValue' }
    keyval_test = requests.post(f'http://{hostName}:80/keyval', json=payload).json()
    result= {'key': 'testKey', 'value': 'testValue', 'command': 'key is testKey and the value is testValue', 'result': False, 'error': 'Key already exists'} 
    assert keyval_test == result

# GET
def test_valid_get():
    slack_test = requests.get(f'http://{hostName}:80/keyval/testKey').json()
    result= {'key': 'testKey', 'value': 'testValue', 'command': 'RETRIEVE testKey', 'result': True, 'error': None } 
    assert slack_test == result

# PUT
def test_valid_put():
    payload = { 'key': 'testKey', 'value': 'newTestValue' }
    keyval_test = requests.put(f'http://{hostName}:80/keyval', json=payload).json()
    result= {'key': 'testKey', 'newvalue': 'newTestValue', 'command': 'key is testKey and the new value is newTestValue', 'result': True, 'error': ''} 
    assert keyval_test == result

# DELETE
def test_valid_delete():
    keyval_test = requests.delete(f'http://{hostName}:80/keyval/testKey').json()
    result= {'key': 'testKey', 'value': 'newTestValue', 'command': 'DELETE testKey', 'result': True, 'error': None} 
    assert keyval_test == result

def test_invalid_delete():
    keyval_test = requests.delete(f'http://{hostName}:80/keyval/testKey').json()
    result= {'key': 'testKey', 'value': None, 'command': 'DELETE testKey', 'result': False, 'error': 'Key does not exist'} 
    assert keyval_test == result

# invalid GET
def test_invalid_get():
    slack_test = requests.get(f'http://{hostName}:80/keyval/testKey').json()
    result= {'key': 'testKey', 'value': None, 'command': 'RETRIEVE testKey', 'result': False, 'error': 'Key does not exist'} 
    assert slack_test == result

#invalid PUT
def test_invalid_put():
    payload = { 'key': 'testKey', 'value': 'newTestValue' }
    keyval_test = requests.put(f'http://{hostName}:80/keyval', json=payload).json()
    result= {'key': 'testKey', 'newvalue': 'newTestValue', 'command': 'key is testKey and the new value is newTestValue', 'result': False, 'error': 'Key does not exist'} 
    assert keyval_test == result