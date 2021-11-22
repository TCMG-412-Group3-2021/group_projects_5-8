from flask import Flask, json, jsonify, request, Response
import typer
import requests

app = typer.Typer()

f = open('./hostName.txt', 'r')
hostName = f.readline()

@app.command()
def keyval(method: str, key: str, value: str):
    payload = {'key': key, 'value': value}
    response = {}
    
    if method.upper() == 'GET':
        response = requests.get(f'http://{hostName}:80/keyval/{key}').json()
    elif method.upper() == 'POST':
        response = requests.post(f'http://{hostName}:80/keyval', json=payload).json()
    elif method.upper() == 'PUT':
        response = requests.put(f'http://{hostName}:80/keyval', json=payload).json()
    elif method.upper() == 'DELETE':
        response = requests.delete(f'http://{hostName}:80/keyval/{key}').json()
    else:
        typer.echo(f'Error: Invalid method \'{method}\'!')
        raise typer.Exit(code = 1)
    
    if response['error']:
        typer.echo(f'Error: {response["error"]}')
        raise typer.Exit(code = 1)
    elif 'RETRIEVE' in response['command']:
        typer.echo(f'The key \'{response["key"]}\' has a value of {response["value"]}')
    


@app.command()
def md5(string: str):
    response = requests.get(f'http://{hostName}:80/md5/{string}').json()
    typer.echo(f'The MD5 hash of \'{string}\' is {response["output"]}')

@app.command()
def factorial(number: str):
    response = requests.get(f'http://{hostName}:80/factorial/{number}').json()
    typer.echo(f'\'{number}\' factorial is {response["output"]}')

@app.command()
def is_prime(number: str):
    response = requests.get(f'http://{hostName}:80/is-prime/{number}').json()
    typer.echo(f'\'{number}\' is indeed a prime number') if response["output"] else typer.echo(f'\'{number}\' is NOT a prime number')

@app.command()
def fibonacci(number: str):
    response = requests.get(f'http://{hostName}:80/fibonacci/{number}').json()
    typer.echo(f'This is the fibonacci sequence up to the number \'{number}\'')
    typer.echo(response['output'])

@app.command()
def slack_alert(message: str):
    response = requests.get(f'http://{hostName}:80/slack-alert/{message}').json()
    typer.echo('Your message was sent successfully! Check out Slack to see it!') if response["output"] else typer.echo(response["output"])


if __name__ == "__main__":
    app()