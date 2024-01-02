# Найдите корень Меркла для транзакций tx0, tx1, tx2, tx3

import hashlib

tx0 = "tx0".encode()
tx1 = "tx1".encode()
tx2 = "tx2".encode()
tx3 = "tx3".encode()
tx4 = "tx4".encode()

hash0 = hashlib.sha256(tx0).hexdigest()
hash1 = hashlib.sha256(tx1).hexdigest()
hash2 = hashlib.sha256(tx2).hexdigest()
hash3 = hashlib.sha256(tx3).hexdigest()
hash4 = hashlib.sha256(tx4).hexdigest()

hash01 = hashlib.sha256((hash0+hash1).encode()).hexdigest()
hash23 = hashlib.sha256((hash2+hash3).encode()).hexdigest()
hash44 = hashlib.sha256((hash4+hash4).encode()).hexdigest()

hash0123 = hashlib.sha256((hash01+hash23).encode()).hexdigest()
hash4444 = hashlib.sha256((hash44+hash44).encode()).hexdigest()

Merkle = hashlib.sha256((hash0123+hash4444).encode()).hexdigest()

print(Merkle)