#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:38:38 2021
"""
def checkPrime(number):
    isPrime = False
    if number == 2:
        isPrime = True
    if number > 2:
        isPrime = True
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
                break

    if isPrime:
        print('Output: True')
    else:
        print('Output: False.',number, 'is not a Prime Number')

if __name__ == '__main__':
    userInput = int(input('Input: '))
    if(userInput>1):
        checkPrime(userInput)
    else:
        print("Output: Sorry, input number must be greater than 1.")
        


