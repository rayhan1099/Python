a = list(map(int,input("Enter: ").split()))
n = len(a)
for i in range(0,n):
    h1=max(a[0],a[i])
    h2=min(a[0],a[i])

for i in range(1,n):
    if(a[i]>h1):
        h2=h1
        h1=a[i]
    elif(a[i]<h1 and a[i]>h2):
        h2=a[i]  
print("Second Highest: ",h2)