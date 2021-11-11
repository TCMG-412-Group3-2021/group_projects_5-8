from flask import Flask, json, jsonify, request, Response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os
import hashlib
import redis
from redis import RedisError, Redis
import typer
import requests

addy = 'http://192.168.1.9:80/' #enter generated ipaddress here

r = redis.StrictRedis(host='localhost', port=6379)

app = typer.Typer()

payload = request.get_json()
v = payload["value"]
k = payload["key"]


#key-val endpoints
@app.command()
def key_val_post():
    r.set(k,v)
    return(f'http POST {addy}/keyval key = {k} value = {v}' )

@app.command()
def key_val_put():
    r.set(k,v)
    return(f'http PUT {addy}/keyval key = {k} value = {v}' )

@app.command()
def key_val_get():
    r.set(k,v)
    return(f'http GET {addy}/keyval key = {k} value = {v}' )

@app.command()
def key_val_delete():
    r.set(k,v)
    return(f'http DELETE {addy}/keyval key = {k} value = {v}' )


#Math/md5/slack end-points
@app.command()
def md5(word: str):
    return(f'{addy}/md5/{word}')

@app.command()
def factorial(number: int):
    return(f'{addy}/factorial/{number}')

@app.command()
def prime(number: int):
    return(f'{addy}/is-prime/{number}')

@app.command()
def fib(number: int):
    return(f'{addy}/fibonacci/{number}')

@app.command()
def fib(message: str):
    return(f'{addy}/slack-alert/{message}')


if __name__ == "__main__":
    app()