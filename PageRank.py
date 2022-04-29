from scipy import linalg
import numpy as np
import pandas as pd

'''Declaring the variables to store the number of webpages(i.e. the number of nodes) in the graph,
   the number and the individual connections between the webpages in the form of hyperlinks,
   the value of probability for random teleportations and the 
   transition matrix with as well as without random teleportations.'''

nodes = int(input("Enter the number of nodes\n")) #Accepting number of nodes in graph 

con = int(input("Enter the number of connections\n")) #Accepting number of connections in graph

randomTeleportationsProbabilty=0.1  #Hyper-parameter for random teleportations

i=0

connections=[]     #List to store the directed edges of the graph
PTM=[]             #Double dimensional matrix to store the transition matrix without random teleportation
PTMRT=[]           #Double dimensional matrix to store the transition matrix with random teleportation

'''Accepting the connections in the graph which signify the movement from one web-page to another
   in the form of hyperlinks which can be clicked upon.'''

#Accept the connections of the graph from the user and store it in a lis
print("Enter the start and end points for each connection\n")
while(i<con):
    start = int(input())
    end = int(input())
    connections.append([start,end])
    i=i+1

outcon=[]   #List to store the number of out-going hyperlinks from a specific node
j=1

'''Iterating through all the connections to calculate the number of outgoing links from that node
   to calculate the number of pages that can be reached from that webpage.'''

#Iteration through the connections to count the number of outgoing connections from a node
while(j<=nodes):
    cnt=0
    for i in connections:
        if i[0]==j:
            cnt=cnt+1
    outcon.append(cnt)
    j=j+1


'''Calculating and constructing the probability transition matrix of the graph in both the following cases:
    1. With random teleportations from one webpage to another
    2. Without random teleportations from one webpage to another'''

#Constructing the probability transition matrix for the case of with and without random teleportations
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
    
'''Using python's linear algebra module in the scientific calculations library to calculate the
   eigenvalues and the left eigenvectors of the probability transition matrix without random teleportations.'''

#Using the linear algebra module in scipy to calculate the eigenvalues and the left eigenvectors
#of the probability transition matrix without random teleportations
eigenval,eigenleftvector=linalg.eig(a=np.array(PTM),b=None,left=True,right=False,overwrite_a=False,overwrite_b=False,check_finite=False)

'''Iterating though the eigenvalues to find the index at which the eigenvalue is one
   and store the corresponding eigenvector in the resultant column matrix.'''

#Since the probability transition matrix is a stochastic matrix
#the principal left eigenvector will be for the eigenvalue of one
#Iterate through the eigen value matrix obtained to find at which index the value is one
#The column at that index is the principal left eigenvector
res=[]
index=0
for x in eigenval:
    if x==1:
        res.append(eigenleftvector[:,index])
    index=index+1

'''Displaying the principal left eigenvalue which indicates the probability of being on each webpage.
   The higher the probability, the greater rank of that web-page.
   The lower the probability, the smaller rank of that web-page.'''

#Displaying the principal left eigenvector which indicated the probability of reaching the webpage with that node value
print("Principal Left Eigenvector without Random Teleportations:\n")
for x in res:
    for j in x:
        print(j,end="  ")
    print("\n")

'''Using python's linear algebra module in the scientific calculations library to calculate the
   eigenvalues and the left eigenvectors of the probability transition matrix with random teleportations.'''

#Using the linear algebra module in scipy to calculate the eigenvalues and the left eigenvectors
#of the probability transition matrix with random teleportations
eigenval,eigenleftvector=linalg.eig(a=np.array(PTMRT),b=None,left=True,right=False,overwrite_a=False,overwrite_b=False,check_finite=False)

'''Iterating though the eigenvalues to find the index at which the eigenvalue is one which is the 
   maximum value and store the corresponding eigenvector in the resultant column matrix.'''

#Since the probability transition matrix with random teleportation is also a stochastic matrix
#the principal left eigenvector will be for the eigenvalue of one
#Iterate through the eigen value matrix obtained to find at which index the value is one (the maximum value)
#The column at that index is the principal left eigenvector
res=[]
index=0
maxeigenvalue=0
maxeigenvalueindex=0
for x in eigenval:
    if x>maxeigenvalue:
        maxeigenvalue=x
        maxeigenvalueindex=index
    index=index+1

#Storing the value of the principal left eigenvector
res.append(eigenleftvector[:,maxeigenvalueindex])

'''Displaying the principal left eigenvalue which indicates the probability of being on each webpage.
   The higher the probability, the greater rank of that web-page.
   The lower the probability, the smaller rank of that web-page.'''

#Displaying the principal left eigenvector which indicated the probability of reaching the webpage with that node value
print("Principal Left Eigenvector with Random Teleportations:\n")
for x in res:
    for j in x:
        print(j,end="  ")
    print("\n")  

