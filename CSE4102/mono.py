import random
a = 'abcdefghijklmnopqrstuvwxyz'
print(a)
key = list(a)
random.shuffle(key)
key = ''.join(key)
print(key)
def encrypt(plaintext):
    ciphertext = ''
    for letter in plaintext:
        if letter.lower() in a:
            index = a.index(letter.lower())
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
        if letter.lower() in a:
            index = key.index(letter.lower())
            if letter.isupper():
                plaintext += a[index].upper()
            else:
                plaintext += a[index]
        else:
            plaintext += letter
    return plaintext

plaintext =str(input("Enter a text: "))
print("Your text is: ",plaintext)
ciphertext = encrypt(plaintext)
print(ciphertext)
decrypted_text = decrypt(ciphertext)
print(decrypted_text)