class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

        
        
    def __iter__(self):
        return iter(self.vertList.values())
    
g = Graph()
n = int(input())
i = 0
lista = []
oi = []
while i < n:
    lista.append(input().split())
    d = g.addVertex(lista[i][0])
    oi.append(d)
    
    i+=1

for a in lista:
    for i in range(int(a[1])):
        g.addEdge(a[0], a[2+i])
        
        
g2 = Graph()
a = input()
n = int(input())
i = 0
lista2 = []
while i < n:
    lista2.append(input().split())
    g2.addVertex(lista2[i][0])   
    i+=1

for a in lista2:
    for i in range(int(a[1])):
        g2.addEdge(a[0], a[2+i])
        
c = True       
for a in g2:
    if c:
        for b in a.getConnections():
            a1 = g.getVertex(a.getId())
            b1 = g.getVertex(b.getId())
            if b1 in a1.getConnections():
                c = True
            else:
                c = False
                break

for a in g2:
    a1 = g.getVertex(a.getId())
    if a1 == None:
        c = False
        break
               
if c:
    print('Sub-sub!')
else:
    print('Ue? Ue? Ue?')
       


        
        