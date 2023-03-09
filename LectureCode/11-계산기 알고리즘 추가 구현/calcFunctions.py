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

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(roman):

    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = 0

    for i in range(len(romans)):
        if roman.startswith(romans[i][1]):
            if i == 0: continue
            for j in range(i):
                if 'CM' or 'CD' or 'XC' or 'XL' or 'IX' or 'IV' in roman and roman[1] == romans[j][1]:
                    continue
                if romans[j][1] in roman[len(romans[i][1]):]:
                    return 'Error!'

    max_count = 0
    count = 0
    for i in range(len(roman) - 1):
        if roman[i] == roman[i + 1]:
            count += 1
        else:
            if max_count < count:
                max_count = count
                count = 0
    if max_count + 1 >= 4:
        return 'Error!'

    for value, letters in romans:
        while roman.startswith(letters):
            result += value
            roman = roman[len(letters):]


    return str(result)

