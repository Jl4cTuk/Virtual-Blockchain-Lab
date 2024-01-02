import hashlib

to_hash = input()
# to_hash = 'Hello World!'


nonce = 0
for i in range(1,4):
    while (1):
        tmp = (to_hash + str(nonce)).encode()
        hash = hashlib.sha256(tmp).hexdigest()
        if hash[0:i] == "0"*i :
            print (nonce)
            break
        else:
            nonce += 1