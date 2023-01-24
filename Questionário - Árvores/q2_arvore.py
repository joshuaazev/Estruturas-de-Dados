# A classe ArvoreBinaria já foi definida

def rotaciona_esquerda(raiz):
    if raiz and raiz.dir:
        aux = raiz
        raiz = raiz.dir
        aux.dir = raiz.esq
        raiz.esq = aux
    
    return raiz