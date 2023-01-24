class Grafo:
    def __init__(self):
        self.arestas = []
        self.vertices = []
    
    def insere_v(self,idt,dado):
        self.vertices.append((idt,dado))
        
    def insere_a(self,ido,idd):
        t0 = False
        t1 = False
        for a in self.vertices:
            if a[0] == ido:
                t0 = True
            elif a[0] == idd:
                t1 = True
        if t1 and t0:
            self.arestas.append((ido,idd))
    
    def remove_v(self,idt):
        for a in range(len(self.vertices)):
            if self.vertices[a][0] == idt:
                del self.vertices[a]
                break
        l = [item for item in self.arestas]
        for a in range(len(l)):
            if l[a][0] == idt or l[a][1] == idt:
                self.arestas.remove(l[a])
    
    def remove_a(self,ido,idd):
        for a in range(len(self.arestas)):
            if self.arestas[a] == (ido,idd):
                del self.arestas[a]
                return
            
    def grau_saida(self,idt):
        c = 0
        for a in range(len(self.arestas)):
            if self.arestas[a][0] == idt:
                c += 1
        return c
    
    def grau_entrada(self,idt):
        c = 0
        for a in range(len(self.arestas)):
            if self.arestas[a][1] == idt:
                c += 1
        return c
        
    def alcancavel(self,id1,id2):
        if (id1,id2) in self.arestas:
            return True
        else:
            for a in self.arestas:
                if a[0] == id1:
                    c = self.alcancavel(a,id2)
                    if c:
                        return True
        return False
            

grafo = Grafo()
n = int(input())
i = 0
while i < n:
    s = input().split()
    if s[0] == 'IV':
        grafo.insere_v(s[1],s[2])    
    elif s[0] == 'IA':
        grafo.insere_a(s[1],s[2])
    elif s[0] == 'RA':
        grafo.remove_a(s[1],s[2])
    elif s[0] == 'RV':
        grafo.remove_v(s[1])
    i+=1



