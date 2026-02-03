from random import randint

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
        return True;

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

n = genNumber()
p = calcNumber(n)

while isPrime(p,10) == False:
    n = genNumber()
    p = calcNumber(n)

