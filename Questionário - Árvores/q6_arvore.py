class ArvoreBinaria:
    def __init__(self, dado=None, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
        
contador = 0
def mostra(raiz):
    global contador
    if raiz == None:
        print('()')
    else:
        if contador == 0:
            contador+=1
            print('(', end='')
            print(str(raiz.dado), end = '')
            if raiz.esq:
                mostra(raiz.esq)
            else:
                print(' ()',end = '')
            if raiz.dir:
                mostra(raiz.dir)
            else:
                print(' ()',end = '')
            contador = 0
            print(')',end = '')
        else:
            print(' (', end='')
            print(str(raiz.dado), end = '')
            if raiz.esq:
                mostra(raiz.esq)
            else:
                print(' ()',end = '')
            if raiz.dir:
                mostra(raiz.dir)
            else:
                print(' ()',end = '')
            print(')',end = '')

testa = False
contador2 = 0
contador = 0
raiz2 = 8888
def nivel(raiz,n):
    global contador
    global contador2
    global testa
    global raiz2
    if contador2 == 0:
        raiz2 = raiz
    if raiz == None:
        return
    if int(str(raiz.dado)) == n:
        if contador2 == 0:
            return 0
        testa = True
        return 0
    else:
        contador2+=1
        nivel(raiz.esq,n)
        if testa:
            contador += 1
        else:
            nivel(raiz.dir,n)
            if testa:
                contador += 1
          
        if raiz2 != raiz:
            return
        else:
            z = contador
            contador = 0
            contador2 = 0
            testa = False
            raiz2 = 888
            return z if z != 0 else -1
        
    
def rotaciona_direita(raiz):
    if not raiz == None:
        if not raiz.esq == None:
            a = raiz
            c = raiz.esq
            d = raiz.esq.esq
            e = raiz.esq.dir
            raiz = c
            raiz.dir = a
            raiz.esq = d
            raiz.dir.esq = e
            return raiz
    return raiz

def esquerda_no_nivel(raiz,n):
    i = n
    r = raiz
    for a in range (n-1,-1,-1):
        r = raiz
        x = a
        y = n-a-1
        while x:
            if not r == None:
                r = r.esq
            x-=1
        while y:
            if not r == None:
                r = r.dir
            y-=1
        if r != None: return r
    return None
            
    
    
    
c = 0
raizz = 0
numm = 0
def comprime(raiz, numero):
    global c
    global raizz
    global numm
    if numero > 0:
        if c == 0:
            raiz = rotaciona_direita(raiz)
            raizz = raiz
            numm = numero
#             mostra(raiz)
#             print()
#             print()
        if c == 0 and numero == 1:
            return raiz
        c+=1
        if numero > 1:
            x1 = esquerda_no_nivel(raiz,c)
            x2 = esquerda_no_nivel(raiz,c+1)
            x3 = rotaciona_direita(x2) 
            x1.esq = x3
#             print('%s\n%s\n%s'%(x1.dado,x2.dado,x3.dado))
#             print('numero = %d' %numero)
#             mostra(raiz)
#             print()
            comprime(raiz,numero-1)
        if raizz == raiz and numm == numero:
            c = 0
        return raiz
    
    
      
  
n1 = ArvoreBinaria('1')        
n2 = ArvoreBinaria('2')
n3 = ArvoreBinaria('3')
n4 = ArvoreBinaria('4')
n5 = ArvoreBinaria('5')
n6 = ArvoreBinaria('6')
n7 = ArvoreBinaria('7')
n8 = ArvoreBinaria('8')
n9 = ArvoreBinaria('9')
n10 = ArvoreBinaria('10')
n11 = ArvoreBinaria('11')
n12 = ArvoreBinaria('12')
n13 = ArvoreBinaria('13')
n14 = ArvoreBinaria('14')
n15 = ArvoreBinaria('15')

# n15.esq = n14
# n14.esq = n13
# n13.esq = n12
# n12.esq = n11
# n11.esq = n10
# n10.esq = n9
# n9.esq = n8
# n8.esq = n7
# n7.esq = n6
# n6.esq = n5
# n5.esq = n4
# n4.esq = n3
# n3.esq = n2
# n2.esq = n1
# 
# mostra(comprime(n15,7))
# print()

# n2.esq = n1
# n2.dir = n3
# mostra(comprime(n2,1))
# print()

n14.esq = n12
n14.dir = n15
n12.dir = n13
n12.esq = n10
n10.dir = n11
n10.esq = n8
n8.dir = n9
n8.esq = n6
n6.dir = n7
n6.esq = n4
n4.dir = n5
n4.esq = n2
n2.dir = n3
n2.esq = n1

mostra(comprime(n14,3))

