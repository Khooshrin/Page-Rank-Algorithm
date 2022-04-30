import numpy as np
import networkx as nx

G=nx.read_gpickle("C:/Users/KHOOSHRIN/Documents/BITS PILANI HYDERABAD CAMPUS/Second Year/Second Semester/CS F469 - Information Retrieval/Assignment II/web_graph.gpickle")

nodes=list(G.nodes)
edges=list(G.edges)

pagecontent=[]
i=0
while(i<100):
    pagecontent.append(G.nodes[i]['page_content'])
    i=i+1

query=input("Enter query:\n")

rootset=[]
baseset=[]
index=0

for x in pagecontent:
    if x.find(query)!=-1:
        rootset.append(index+1)
        baseset.append(index+1)
    index=index+1

for x in rootset:
    inedges=G.in_edges(x)
    outedges=G.out_edges(x)
    for e in inedges:
        if e not in baseset:
            baseset.append(e[0])
    for e in outedges:
        if e not in baseset:
            baseset.append(e[1])

AdjacencyMatrix=[]

for e1 in baseset:
    temp=[]
    for e2 in baseset:
        if (e1,e2) in edges:
            temp.append(1)
        else:
            temp.append(0)
    AdjacencyMatrix.append(temp)

hub_outdegree=[]
auth_indegree=[]

for x in baseset:
    hub_outdegree.append(len(G.out_edges(x)))
    auth_indegree.append(len(G.in_edges(x)))

matrix=np.array(AdjacencyMatrix)
TransposeAdjacencyMatrix=matrix.T

u=np.ones(len(baseset))
v=np.ones(len(baseset))

while(True):
    v=np.dot(TransposeAdjacencyMatrix,u)
    u=np.dot(AdjacencyMatrix,v)

    v=v/np.linalg.norm(v)
    u=u/np.linalg.norm(u)

    subu=np.subtract(hub_outdegree,u)
    subv=np.subtract(auth_indegree,v)
    chk=0

    for a in subu:
        if abs(a)>0.001:
            chk=1

    for a in subu:
        if abs(a)>0.001:
            chk=1

    if chk==0:
        break
    else:
        hub_outdegree=u
        auth_indegree=v

index=0

print("Hub Scores:\nNode\tScore")

for a in u:
    print(baseset[index],end="\t")
    print(a,end="\n")
    index=index+1

index=0

print("Authority Scores:\nNode\tScore")

for a in v:
    print(baseset[index],end="\t")
    print(a,end="\n")
    index=index+1