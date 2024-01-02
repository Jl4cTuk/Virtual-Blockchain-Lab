import rsa

pubA, privA = rsa.newkeys(2048)
pubB, privB = rsa.newkeys(2048)

M = 'Криптографические основы технологии блокчейн'
CT = rsa.encrypt(M.encode('utf-8'), pubA)

OT = rsa.decrypt(CT, privA)

Sign = rsa.sign(M.encode('utf-8'), privB, 'SHA-256')
Verify = rsa.verify(M.encode('utf-8'), Sign, pubB)

print('Original Message:', M)
print('Encrypted Message:', CT)
print('Decrypted Message:', OT.decode('utf-8'))
print('Signature:', Sign)
print('Verification Result:', Verify)
