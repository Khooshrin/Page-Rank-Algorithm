import networkx as nx
import array as arr
import numpy as np
from scipy import linalg

web_graph=nx.read_gpickle("C:/Users/KHOOSHRIN/Documents/BITS PILANI HYDERABAD CAMPUS/Second Year/Second Semester/CS F469 - Information Retrieval/Assignment II/web_graph.gpickle")
print(web_graph)

#read all the queries
query = input('Enter your query:')
query = query.split()

inarr = np.zeros(100)

for i in range(0,100) :
    node_index = i
    doc = web_graph.nodes[node_index]['page_content']
    arr0=doc.split()

#create an array arr0 for storing all values
    for q in query:
        if q in arr0:
            inarr[i]=1
            break

#create adjacency matrix arr1
arr1=nx.to_numpy_array(web_graph)
inarr=np.array(inarr)
#arr2=inarr*arr1
arr2=np.dot(inarr,arr1)
#arr3=inarr * (arr1)T
arr3=np.dot(inarr,arr1.T)
#arr4=inarr+arr2+arr3
arr4=np.add(inarr,np.add(arr2,arr3))
#create the baseset
arr5=[]

for i in range (0,99):
    if(arr4[i]!=0):
        #add i to a vector arr5
        arr5.append(i)

#create a subgraph using arr5
subgraph=nx.subgraph(web_graph, arr5)
arr8=nx.to_numpy_array(subgraph)

hubvector=np.ones(len(arr5))
authvector=np.ones(len(arr5))
hubvector=hubvector/sum(hubvector)
authvector=authvector/sum(authvector)


count=0
while(count<=1000):
    hubvector=np.dot(arr8,authvector)
    authvector=np.dot(arr8.T,hubvector)
    hubvector=hubvector/sum(hubvector)
    authvector=authvector/sum(authvector)
    count=count+1

arr5=list(subgraph.nodes)

print("\nNode\tHub Values:")
index=0
for x in hubvector:
    print(arr5[index],end="\t")
    print(x,end="\n")
    index=index+1

print("\nNode\tAuthority Values:")
index=0
for x in authvector:
    print(arr5[index],end="\t")
    print(x,end="\n")
    index=index+1