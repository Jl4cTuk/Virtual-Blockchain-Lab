import math

def gcd(f):
    e = 2
    while (1):
        if (math.gcd(e,f) == 1):
            break
        else:
            e+=1
    return e

def find_d(e, f):
    d = 1
    while (1):
        if ((e*d)%f == 1):
            break
        else:
            d+=1
    return d

p = int(input())
q = int(input())

n = p*q

f = (p-1)*(q-1)

e = gcd(f)

print ("Public key: (", e, ';', n, ')') 
print("Private key: (", find_d(e, f), ';', n, ')')