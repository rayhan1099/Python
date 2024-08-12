Dict={'rayhan':99,'arman':56,'sanvi':59,'shaikot':57}
print("length : %d" %  len (Dict))
Dict2={'rayhan':99,'arman':56,'shaikot':57}
Dict3={'sanvi':59}
for key in list(Dict.keys()) :
    if key in list(Dict2.keys()):
        print(True)
    else:
        print(False) 
students=list(Dict.keys())
students.sort()
for S in students:
    print(":".join ((S,str(Dict[S]))))