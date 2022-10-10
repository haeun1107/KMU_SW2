from math import factorial as fact


def funcList(num, numStr):
    if num == 0:
        return factorial(numStr)
    if num == 1:
        return decToBin(numStr)
    if num == 2:
        return binToDec(numStr)
    if num == 3:
        return decToRoman(numStr)
    if num == 4:
        return romanToDec(numStr)

def factorial(numStr):
    n = int(numStr)
    r = str(fact(n))
    return r

def decToBin(numStr):
    n = int(numStr)
    r = bin(n)[2:]
    return r

def binToDec(numStr):
    n = int(numStr, 2)
    r = str(n)
    return r

def decToRoman(numStr):
    n = int(numStr)
    if n >= 4000:
        return 'Error!'
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    return result

def romanToDec(numStr):
    s = numStr
    N = 0
    dec = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
        ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
        ('X', 10), ('IX', 9), ('V', 5), ('IV', 4),
        ('I', 1)
    ]
    try:
        for value, letters in dec:
            while s.find(value) == 0:
                N += letters
                if len(value) == 1:
                    s = s[1:]
                if len(value) == 2:
                    s = s[2:]
        return N
    except:
        return 'Error!'