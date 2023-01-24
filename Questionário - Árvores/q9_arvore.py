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

cont1 = 0
ppp = 0
def cria_arvore(lista,raiz = None):
    global cont1
    global ppp
    if cont1 == 0:
        raiz = ArvoreBinaria(lista[cont1])
        ppp = raiz
    cont1+=1
   
    if not lista[cont1] == None:
        raiz.esq = ArvoreBinaria(lista[cont1])
        cria_arvore(lista,raiz.esq)
    cont1+=1
    if not lista[cont1] == None:
        raiz.dir = ArvoreBinaria(lista[cont1])
        cria_arvore(lista,raiz.dir)

cont2 = 0
rbd = 0
def altura(raiz):
    global cont2
    global rbd
    if cont2 == 0:
        rbd = raiz
        cont2 += 1
    if raiz == None:
        return            
    h_esq = 0
    h_dir = 0
    if raiz.esq:
        h_esq = altura(raiz.esq)
    if raiz.dir:
        h_dir = altura(raiz.dir)
    if rbd == raiz:
        cont2 = 0
        return h_esq - h_dir
    return h_dir + 1 if h_dir > h_esq else h_esq + 1


def toda_arvore(raiz):
    if raiz == None:
        return
    raiz.dado = altura(raiz)
    toda_arvore(raiz.esq)
    toda_arvore(raiz.dir)



a = input()
lista = []
n = len(a)
for i in range(n):
    if a[i] == '(':
        if a[i+1] == ')':
            lista.append(None)
        else:
            lista.append(a[i+1])
            
cria_arvore(lista)
toda_arvore(ppp)
mostra(ppp)


        