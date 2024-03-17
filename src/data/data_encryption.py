import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib


class DataEncryption:

    def __init__(self):
        self.key = 
        self.cipher = AES.new(self.key, AES.MODE_EAX)

    def encrypt(self, file_name):
        with open(file_name, "rb") as f:
            data = f.read()
        ciphertext, tag = self.cipher.encrypt_and_digest(data)

        with open(file_name + ".enc", "wb") as f:
            [f.write(x) for x in (self.cipher.nonce, tag, ciphertext)]

    def decrypt(self, file_name):
        with open(file_name, "rb") as f:
            nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
