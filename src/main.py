#!/usr/bin/env python3
from datetime import *
from hashlib import *
from binascii import unhexlify, hexlify

class Block:
    def __init__(self, prev_hash, transaction, amount):
        self.next = None
        self.__data = {
            "prev_hash": prev_hash,
            "transaction": transaction,
            "amount": amount,
            "hash": "",
            "time": datetime.now().time()
        }
        self.__data["hash"] = self.make_hash()

    def get_data(self):
        return self.__data
    
    def make_hash(self):
        new_hash = hexlify(sha256(unhexlify(self.get_data()["prev_hash"])).digest()).decode("utf-8")
        while new_hash[:5] != "00000":
            new_hash = hexlify(sha256(unhexlify(new_hash)).digest()).decode("utf-8")
        return new_hash
    
    def append(self, transaction, amount):
        n = self
        while n.next:
            n = n.next
        prev_hash = n.get_data()["hash"]
        end = Block(prev_hash, transaction, amount)
        n.next = end

def print_blocks(block):
    node = block
    print(node.get_data(), "\n")
    while node.next:
        node = node.next
        print(node.get_data(), "\n")

if __name__ == "__main__":
    my_block = Block("0000f5fe09f0c817844ca2a6de0898fed095b86930ccc5d9763d8c87da6491ca", "Ivan", 10)
    my_block.append("Dimka", 1337)
    my_block.append("6opucbl4", 5555)
    print_blocks(my_block)