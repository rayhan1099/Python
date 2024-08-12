def com(h,r):
    if(h<=40):
        return h*r
    if(h>40):
        return ((40*r)+(h-40)*r*1.5)
h=float(input(""))
r=float(input(""))
p=com(h,r)
print(p)