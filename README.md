## Getting Started
1. In order to run this program, you must copy the ```.envCOPY``` file and rename it to ```.env```
2. In ```.env```, add the correct slack bot api token
3. Run the ```app.py``` file with the command ```python3 app.py```
4. Go to ```localhost:3000``` on your local browser and try one of the following API endpoints:
- /md5/ 
- /fibonacci/
- /slack-alert/
## CLI 
1. This is the following template for the commands ```python3 cli.py [API ENDPOINT] [PARAMETERS]```
2. These are the following API endpoints and their corresponding parameters
    - ```keyval [METHOD] [KEY] [VALUE]```
        - METHODS = 'POST', 'PUT', 'GET', 'DELETE'  
    - ```md5 [STRING TO CONVERT]```
    - ```factorial [NUMBER]```
    - ```fibonacci [NUMBER]```
    - ```is-prime [NUMBER]```
    - ```slack-alert [MESSAGE]```

## Testing
1. Ensure that the IP address within ```hostName.txt``` is updated to match the IP address that the API is running on.
2. Run the command ```pytest``` to run all of the test cases