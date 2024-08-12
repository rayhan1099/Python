def encrypt(mes,k):
    result= ""
    for i in range(len(mes)):
        char = mes[i]
        if (char.isupper()):
            result += chr((ord(char) + k-65)% 26+65)
        elif (char ==" "):
            result +=' '
        elif (char.islower()):
            result += chr((ord(char) + k-97) % 26 + 97)
    return result


mes=input()
k=3
print("mes:"+mes)
encrypt=encrypt(mes,k)
print("encrypt:"+encrypt)


def decrypt(mes, k):
    result = ""
    for i in range(len(mes)):
        char = mes[i]

        if (char.isupper()):
            result += chr((ord(char) - k - 65) % 26 + 65)
        elif (char == " "):
            result += ' '
        elif (char.islower()):
            result += chr((ord(char) - k - 97) % 26 + 97)
    return result

mes =encrypt
k = 3
decrypt=decrypt(mes,k)
print("decrypt:"+decrypt)