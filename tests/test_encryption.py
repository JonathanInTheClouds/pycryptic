import pytest
from pycryptic.encryption import encrypt, decrypt

def test_encryption_decryption():
    password = "strongpassword"
    data = b"Hello, pycryptic!"
    
    # Encrypt and decrypt the data
    encrypted_data = encrypt(data, password)
    decrypted_data = decrypt(encrypted_data, password)
    
    # Verify that decryption returns the original data
    assert decrypted_data == data

def test_encryption_wrong_password():
    password = "correctpassword"
    wrong_password = "wrongpassword"
    data = b"Secret message"

    # Encrypt with the correct password
    encrypted_data = encrypt(data, password)

    # Attempt to decrypt with the wrong password
    with pytest.raises(Exception):  # Cryptography library raises exceptions on failure
        decrypt(encrypted_data, wrong_password)

def test_encrypt_empty_data():
    password = "testpassword"
    data = b""
    encrypted_data = encrypt(data, password)
    decrypted_data = decrypt(encrypted_data, password)
    assert decrypted_data == data

def test_encrypt_large_data():
    password = "testpassword"
    data = b"A" * 10**6  # 1 MB of data
    encrypted_data = encrypt(data, password)
    decrypted_data = decrypt(encrypted_data, password)
    assert decrypted_data == data

def test_encrypt_binary_data():
    password = "testpassword"
    data = b"\x00\xFF\xFE\xFD\xFC"  # Binary data
    encrypted_data = encrypt(data, password)
    decrypted_data = decrypt(encrypted_data, password)
    assert decrypted_data == data

def test_decrypt_invalid_data():
    password = "correctpassword"
    invalid_data = b"this-is-not-valid-encrypted-data"

    with pytest.raises(Exception):  # Expect an error during decryption
        decrypt(invalid_data, password)

def test_encrypt_missing_password():
    with pytest.raises(TypeError):  # Expect a missing argument error
        encrypt(b"Some data")
