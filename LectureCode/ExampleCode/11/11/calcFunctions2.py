from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'
    
    result = ''
    
    while n >= 1000:
        result += 'M'
        n -= 1000
    while n >= 900:
        result += 'CM'
        n -= 900
    while n >= 500:
        result += 'D'
        n -= 500
    while n >= 400:
        result += 'CD'
        n -= 400
    while n >= 100:
        result += 'C'
        n -= 100
    while n >= 90:
        result += 'XC'
        n -= 90
    while n >= 50:
        result += 'L'
        n -= 50
    while n >= 40:
        result += 'XL'
        n -= 40
    while n >= 10:
        result += 'X'
        n -= 10
    while n >= 9:
        result += 'IX'
        n -= 9
    while n >= 5:
        result += 'V'
        n -= 5
    while n >= 4:
        result += 'IV'
        n -= 4
    while n >= 1:
        result += 'I'
        n -= 1
    
    return result

def romanToDec(numStr):
    return 'Roman to Dec'

