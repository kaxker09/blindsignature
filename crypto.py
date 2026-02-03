from random import randint
from math import gcd
import hashlib

def genNumber():
    b = 1024
    n = [0] * b

##zapisywanie liczby do tablicy
    for i in range(len(n)):
        n[i] = randint(0,1)

    n[0] = 1
    n[b-1] = 1
    print(n)
    return n

##odczytywanie licbzy z tablicy i zapisywanie jej do zmiennej
def calcNumber(n):
    p =  0
    for i in range(len(n)):
        temp = n[i]
        if temp == 1:
            x = pow(2,i)
            p += x

    print(p)
    return p

def isPrime(p,k):
    d = p-1

    while d % 2 == 0:
        d //=2

    for i in range(k):
        if (rabinMiller(d,p) == False):
            return False

    print(1)
    return True

def rabinMiller(d,p):
    a = randint(2,p-1)
    x = power(a,d,p)

    if x == 1 or x == p - 1:
        return True

    while d != p - 1:
        x = (x * x) % p
        d *= 2

        if x == 1:
            return False
        if x == p - 1:
            return True

    return False

def power(x,y,p):
    res = 1
    x = x % p
    while y>0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p

    return res

#generating keys for rsa
def genKeys(p,q):
    n = p*q
    f = (p-1)*(q-1)

    while True:
        e = randint(1,f)
        if gcd(e,f) == 1:
            break

    d = d = pow(e, -1, f)

    print(n)
    print(e)
    print("d:", d)
    return e,d

def signature(d):
    with open('text.txt', 'r') as file:
        data = file.read().replace('\n', '')

    h = hashlib.new('sha256')

    h.update(data)

    s = h.hexdigest()
    print(s)
    return s

#def verifySignature(e,p,s):


########
n = genNumber()
p = calcNumber(n)

while isPrime(p,10) == False:
    n = genNumber()
    p = calcNumber(n)

n = genNumber()
q = calcNumber(n)

while isPrime(q,10) == False:
    n = genNumber()
    q = calcNumber(n)


e,d = genKeys(p,q)
signature(d)