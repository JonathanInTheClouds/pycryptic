from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

# Constants

SALT_SIZE = 16
KEY_SIZE = 32
BLOCK_SIZE = 16

def generate_key(password: str, salt: str) -> bytes:
    """Generate a key from a password and a salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt(data: bytes, password: str) -> bytes:
    """Encrypts data using AES-GCM."""
    salt = os.urandom(SALT_SIZE)
    key = generate_key(password, salt)
    iv = os.urandom(BLOCK_SIZE)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    return salt + iv + encryptor.tag + ciphertext

def decrypt(encrypted_data: bytes, password: str) -> bytes:
    """Decrypts data using AES-GCM."""
    salt = encrypted_data[:SALT_SIZE]
    iv = encrypted_data[SALT_SIZE:SALT_SIZE + BLOCK_SIZE]
    tag = encrypted_data[SALT_SIZE + BLOCK_SIZE:SALT_SIZE + BLOCK_SIZE + BLOCK_SIZE]
    ciphertext = encrypted_data[SALT_SIZE + BLOCK_SIZE + BLOCK_SIZE:]
    key = generate_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()