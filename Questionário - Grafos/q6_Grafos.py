
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
condicao = True

while i < n:
    lista.append(input().split())
    d = g.addVertex(lista[i][0])
    
    i+=1

for a in lista:
    for i in range(int(a[1])):
        g.addEdge(a[0],a[2+i])



for a in g:
    if len(a.getConnections()) >= 2:
        for b in a.getConnections():
            for c in a.getConnections():
                if c in b.getConnections():
                    condicao = False

teste = True
for a in g:
    if not len(a.getConnections()) == 2:
        teste = False
        break

if teste == True and n % 2 == 1:
    condicao = False
        
                
if condicao:
    print('Lerei "O Vermelho e o Negro".')
else:
    print('Mais cor, por favor!')
