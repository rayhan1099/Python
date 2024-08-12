def filterdata(x):
    if x>3:
       return x
result=filter(filterdata,(1,2,6,5))
print(list(result))