#!/usr/bin/env python3
from datetime import *
from hashlib import *
from binascii import unhexlify, hexlify
import json
import os

class Block:
    def __init__(self, prev_hash, lender, borrower, amount):
        self.next = None
        self.__data = {
            "prev_hash": prev_hash,
            "lender": lender,
            "borrower": borrower,
            "amount": amount,
            "hash": "",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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

def get_last_block():
    files = os.listdir('blockchain')
    if not files:
        return None
    latest_file = max(files, key=lambda x: int(x.split('_')[1].split('.')[0]))
    with open(f'blockchain/{latest_file}', 'r') as file:
        return json.load(file)

def write_block(lender, borrower, amount):
    blockchain_folder = 'blockchain'
    if not os.path.exists(blockchain_folder):
        os.makedirs(blockchain_folder)

    last_block = get_last_block()
    prev_hash = last_block["hash"] if last_block else '0'*64

    new_block = Block(prev_hash, lender, borrower, amount)

    block_number = len(os.listdir(blockchain_folder)) + 1
    with open(os.path.join(blockchain_folder, f'block_{block_number}.json'), 'w') as file:
        json.dump(new_block.get_data(), file, indent=4)

if __name__ == "__main__":

    pass