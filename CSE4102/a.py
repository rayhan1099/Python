import random
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = list(alphabet)
random.shuffle(key)
key = ''.join(key)

def encrypt(plaintext):
    ciphertext = ''
    for letter in plaintext:
        if letter.lower() in alphabet:
            index = alphabet.index(letter.lower())
            if letter.isupper():
                ciphertext += key[index].upper()
            else:
                ciphertext += key[index]
        else:
            ciphertext += letter
    return ciphertext

def decrypt(ciphertext):
    plaintext = ''
    for letter in ciphertext:
        if letter.lower() in alphabet:
            index = key.index(letter.lower())
            if letter.isupper():
                plaintext += alphabet[index].upper()
            else:
                plaintext += alphabet[index]
        else:
            plaintext += letter
    return plaintext

plaintext = input("Enter the plaintext message: ")
ciphertext = encrypt(plaintext)
print(ciphertext)
decrypted_text = decrypt(ciphertext)
print(decrypted_text)