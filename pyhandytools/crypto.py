# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


class CryptoUtils:
    """
    demo:
        key = 'your-32-bytes-key'
        util = CryptoUtils(key)

        plaintext = 'true_password'
        encrypted = util.encrypt(plaintext)
        print(f'Encrypted: {encrypted}')

        decrypted = util.decrypt(encrypted)
        print(f'Decrypted: {decrypted}')
    """

    def __init__(self, key_: str):
        # Guaranteed length is 32 bytes (256 bits)
        self.key = key_.ljust(32)[:32].encode('utf-8')

    def encrypt(self, plain_text: str):
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plain_text.encode('utf-8'), AES.block_size))

        return base64.b64encode(iv + ciphertext).decode('utf-8')

    def decrypt(self, b64_ciphertext: str):
        ciphertext = base64.b64decode(b64_ciphertext)
        iv = ciphertext[:AES.block_size]
        ciphertext = ciphertext[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = unpad(cipher.decrypt(ciphertext), AES.block_size)

        return plain_text.decode('utf-8')
