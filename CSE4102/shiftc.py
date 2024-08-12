msg=input("Enter a Message: ")
k=int(input("Enter a Key: "))
print("Your En. Message is: ",end='')
enc_msg=[]
for let in msg:
    i=ord(let)
    if(i+k)>90 and i<97 and let!='':
        c=(i+k)%90
        i=65+c
    elif (i+k)>122 and let!='':
        c=(i+k)%122
        i=97+c
    elif let!=' ':
        i=i+k
    enc_msg.append(chr(i))
    print(chr(i),end='') 