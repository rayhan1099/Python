from typing import DefaultDict
from queue import Queue


n=int(input("How many nodes? "))
e=int(input("How many edges? "))
adj=DefaultDict(list)
#adj=[[0 for i in range(n)] for j in range(n)]
#print(adj)
#print("Enter edge information in separate lines")
#for i in range(e):
 #   u,v=map(int,input("Edge %d: "%(i+1)).split())
  #  adj[u][v]=1
   # adj[v][u]=1
#for line in adj:
 #   for element in line:
  #      print(element,end=' ')
   # print()
#adj={}
print("Enter edges' information.")
for i in range(e):
    u,v=input("Edge %d: "%(i+1)).split()
    adj[u].append(v)
    adj[v].append(u)
   # if u not in adj:
    #    adj[u]=[v]
    #else:
     #   adj [u].append(v)
    #if v not in adj:
     #   adj[v]=[u]
    #else:
     #   adj[v].append(u)
visited=set()
q=Queue(maxsize=n)
s=input("Enter Source node: ")
q.put(s)
print("BFS")
while not q.empty():
    u=q.get()
    print(u,end=' ')
for element in adj[u]:
    if element not in visited:
        q.put(element)
        visited.add(element)
#print(adj)
