import math

def find_V (n):
    V = []
    for i in range (1, n):
        x = i**2 % n
        if math.gcd(x, n) == 1:
            if x in V:
                next
            else:
                V.append(x)
    return V

def find_S (v, n):
    S = []
    for i in v:
        j=1
        while (1):
            if (i*j)%n == 1:
                if math.sqrt(j).is_integer():
                    S.append(math.sqrt(j))
                else:
                    while (1):
                        j+=n
                        if math.sqrt(j).is_integer():
                            S.append(math.sqrt(j)%n)
                            break
                break
            else: j+=1
    return S

p = int(input())
q = int(input())
n = p*q

V = find_V(n)
# print(V)

S = find_S(V, n)
# print (S)

PubK = V[0:4]
PrK = S[0:4]
print ("Public key:", PubK)
print ("Private key:", PrK)