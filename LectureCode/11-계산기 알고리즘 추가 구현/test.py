def romanToDec(roman):
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = 0

    # for i in range(1, len(roman)):
    #     if roman[i - 1] == roman[i]:
    #         if roman[i - 1] != roman[i]: break
    #         num += 1
    # return num

    max_count = 0
    count = 0
    for i in range(len(roman) - 1):
        if roman[i] == roman[i + 1]:
            count += 1
        else:
            if max_count < count:
                max_count = count
                count = 0
    return max_count + 1

print(romanToDec('CDXL'))
print(romanToDec('CMLXXXVII'))