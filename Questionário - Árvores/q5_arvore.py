def nivel(raiz, dado):
    if raiz is None:
        return -1
    
    if raiz.dado == dado:
        return 0
    
    nivel_esq = nivel(raiz.esq, dado)
    if nivel_esq >= 0:
        return 1 + nivel_esq
    
    nivel_dir = nivel(raiz.dir, dado)
    if nivel_dir >= 0:
        return 1 + nivel_dir

    return -1