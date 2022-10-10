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
    return 'dec -> Roman'
