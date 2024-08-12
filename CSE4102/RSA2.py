import random
from math import gcd

def generate_keypair(p, q):
    """Generates an RSA public-private key pair."""
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that e and phi(n) are coprime
    e = random.randint(1, phi)
    while gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # Calculate d such that d*e ≡ 1 (mod phi(n))
    d = pow(e, -1, phi)

    return ((e, n), (d, n))

def encrypt(public_key, message):
    """Encrypts a message using an RSA public key."""
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

def decrypt(private_key, ciphertext):
    """Decrypts a ciphertext using an RSA private key."""
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

# Example usage:
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

message = "Hello world"
ciphertext = encrypt(public_key, message)
decrypted = decrypt(private_key, ciphertext)

print("Public key:", public_key)
print("Private key:", private_key)
print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted)
