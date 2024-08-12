
msg = input("Enter a Message: ")
print("Your Encription Message is: ", end='')
EM = []
keys = {'Z': 'C', 'Y': 'B', 'X': 'A', 'z': 'c', 'y': 'b', 'x': 'a', 'C': 'Z',
        'B': 'Y', 'A': 'X', 'c': 'z', 'b': 'y', 'a': 'x', ' ': ' '}
for i in msg:
    if 'X' == i or 'Y' == i or 'Z' == i or 'x' == i or 'y' == i or 'z' == i or ' ' == i:
        EM.append(keys[i])
    else:
        i = ord(i) + 3
        EM.append(chr(i))
    print(EM[len(EM)-1], end='')

print("\nYour Decreption Message is: ", end='')
for j in EM:
    if 'A' == j or 'B' == j or 'C' == j or 'a' == j or 'b' == j or 'c' == j or ' ' == j:
        print(keys[j], end='')
    else:
        i = ord(j) - 3
        print(chr(i), end='')