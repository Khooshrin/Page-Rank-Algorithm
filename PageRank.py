from scipy import linalg
import numpy as np
import pandas as pd

nodes = int(input("Enter the number of nodes\n")) #Accepting number of nodes in graph 

con = int(input("Enter the number of connections\n")) #Accepting number of connections in graph

randomTeleportationsProbabilty=0.1  #hyper-parameter for random teleportations

i=0

connections=[]
PTM=[]
PTMRT=[]

print("Enter the start and end points for each connection\n")
while(i<con):
    start = int(input())
    end = int(input())
    connections.append([start,end])
    i=i+1

outcon=[]
j=1
while(j<=nodes):
    cnt=0
    for i in connections:
        if i[0]==j:
            cnt=cnt+1
    outcon.append(cnt)
    j=j+1

#for i in outcon:
    #print(i,end=" ")

i=0
while(i<nodes):
    temp=[]
    temp1=[]
    j=0
    while(j<nodes):
        chk=0
        for x in connections:
            if x[0]==i+1 and x[1]==j+1:
                temp.append(1/outcon[i])
                temp1.append((1/outcon[i])*randomTeleportationsProbabilty+((1-randomTeleportationsProbabilty)/nodes))
                chk=1
                break
        if chk==0:
            temp.append(0)
            temp1.append(((1-randomTeleportationsProbabilty)/nodes))
        j=j+1
    PTM.append(temp)
    PTMRT.append(temp1)
    i=i+1
    
eigenval,eigenleftvector=linalg.eig(a=np.array(PTM),b=None,left=True,right=False,overwrite_a=False,overwrite_b=False,check_finite=False)

res=[]
index=0
for x in eigenval:
    if x==1:
        res.append(eigenleftvector[:,index])
    index=index+1

print("Principal Left Eigenvector without Random Teleportations:\n")
for x in res:
    for j in x:
        print(j,end="  ")
    print("\n")

eigenval,eigenleftvector=linalg.eig(a=np.array(PTMRT),b=None,left=True,right=False,overwrite_a=False,overwrite_b=False,check_finite=False)

res=[]
index=0
maxeigenvalue=0
maxeigenvalueindex=0
for x in eigenval:
    if x>maxeigenvalue:
        maxeigenvalue=x
        maxeigenvalueindex=index
    index=index+1

res.append(eigenleftvector[:,maxeigenvalueindex])

print("Principal Left Eigenvector with Random Teleportations:\n")
for x in res:
    for j in x:
        print(j,end="  ")
    print("\n")  

