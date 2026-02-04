from random import randint
from math import gcd
import hashlib

def gennumber():
    b = 1024
    n = [0] * b

    for i in range(len(n)):
        n[i] = randint(0,1)

    n[0] = 1
    n[b-1] = 1
    print(n)
    return n

def calcnumber(n):
    p =  0
    for i in range(len(n)):
        temp = n[i]
        if temp == 1:
            x = pow(2,i)
            p += x

    print(p)
    return p

def isprime(p,k):
    d = p-1

    while d % 2 == 0:
        d //=2

    for i in range(k):
        if (rabinmiller(d,p) == False):
            return False

    print(1)
    return True

def rabinmiller(d,p):
    a = randint(2,p-1)
    x = pow(a,d,p)

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

def genkeys():

    while True:
        x = gennumber()
        temp = calcnumber(x)
        if isprime(temp, k=10) == True:
            p = temp
            break

    while True:
        x = gennumber()
        temp = calcnumber(x)
        if isprime(temp, k=10) == True:
            q = temp
            break

    n = p*q
    f = (p-1)*(q-1)

    while True:
        e = randint(1,f)
        if gcd(e,f) == 1:
            break

    d = pow(e, -1, f)

    return n,e,d

def signature(d,n):
    with open('text.txt', 'r') as file:
        data = file.read().replace('\n', '')

    hash_bytes = hashlib.sha256(data.encode('utf-8')).digest()
    h = int.from_bytes(hash_bytes, 'big') % n
    s = pow(h,d,n)
    return s

def blindvar(p,e):
    #unique key to voting
    nv,ev,dv = genkeys()
    while True:
        r = randint(1, p)
        if gcd(r,p) == 1:
            break

    with open("keypriv.txt", "w", encoding="utf-8") as f:
        f.write(f"{dv}\n{r}")

    with open("keypriv.txt", "rb") as f:
        data_bytes = f.read()

    hash_bytes = hashlib.sha256(data_bytes).digest()
    h = int.from_bytes(hash_bytes, "big") % p

    temp = pow(r, e, p)
    t = (temp * h) % p

    return r,t,nv,ev,dv

def blindsignature(t,d,n):
    bs = pow(t,d,n)
    return bs

def verifysignature(e,n,s,h):
    temp = pow(s,e,n)
    if temp == h:
        return True

    return False

def removeblind(r,n,bs):
    rinv = pow(r,-1,n)
    s = (bs * rinv) % n
    return s

def verifyblindsignature(d,n,bs,s,r):
    rinv = pow(r,-1,n)
    temp = pow(bs,rinv,n)
    if temp == s:
        return True

    return False

