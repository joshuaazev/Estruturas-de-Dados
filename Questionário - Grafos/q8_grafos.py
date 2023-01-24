
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
peso = 0
lista = []
while i < n:
    lista.append(input().split())
    d = g.addVertex(lista[i][0])
    
    i+=1

for a in lista:
    for i in range(0,2 * int(a[1]),2):
        g.addEdge(a[0],a[3+i], a[2+i])


lista2 = []
for i in range (n):
    lista2.append([-1,lista[i][0]])

if n > 1:
    lista2[0] = [g.getVertex(lista[0][0]),lista[0][0]]
    true = True
    while true:
        c = []
        for a in lista2:
            if a[0] != -1:
                for b in g.getVertex(a[1]).getConnections():

                    for x in lista2:
                        if x[1] == b.getId():
                            if x[0] == -1:
                                c.append([int(g.getVertex(a[1]).getWeight(b)),g.getVertex(a[1]),b])
        c.sort(key=lambda item:item[0])


        for num in range(len(lista2)):
            if lista2[num][1] == c[0][2].getId():
                lista2[num][0] = c[0][1]
                
        

        
        true = False
        for a in lista2:
            if a[0] == -1:
                true = True

            
        

    for a in range (1, len(lista2)):
        peso += int(lista2[a][0].getWeight(g.getVertex(lista2[a][1])))


print('R$ %.2f' %(peso * 3.14))
    