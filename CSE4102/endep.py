k = int(input("Enter a Key:"))
plaintext = str(input("Enter the sentence:"))

def en_text(plaintext , k):
    ans = ""
    for i in range(len(plaintext)):
        c = plaintext[i]

        if c == " ":
            ans +=" "
        elif (c.isupper()):
            ans += chr((ord(c) + k - 65) % 26 + 65)
        else:
            ans += chr((ord(c) + k - 97) % 26 + 97)

    return ans
def text(en_text):
    ans = ""
    for j in range(len(en_text)):
        c = en_text[j]

        if c == " ":
            ans +=" "
        elif (c.isupper()):
            ans += chr((ord(c) + k - 65) % 26 + 65)
        else:
            ans += chr((ord(c) + k - 97) % 26 + 97)
    return ans
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(k))
print("Cipher Text is : " + en_text(plaintext,k))
print("de Text is : " + text(plaintext,k))
