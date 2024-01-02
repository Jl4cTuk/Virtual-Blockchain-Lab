from ecdsa import SigningKey, NIST384p

sk = SigningKey.generate()
vk = sk.verifying_key

Mes = 'Криптографические основы технологии блокчейн'
Mes = Mes.encode()

signature = sk.sign(Mes)
print(signature.hex())

verify = vk.verify(signature, Mes)
print(verify)

sk_str = sk.to_string().hex()
print (sk_str)

sk2 = SigningKey.from_string(bytes.fromhex(sk_str))
print(sk==sk2)

sk_pem = sk.to_pem()
print(sk_pem)

sk3 = SigningKey.from_pem(sk_pem)
print(sk==sk3)