# A classe ArvoreBinaria já foi definida

def mostra(raiz):
    print("(", end='');

    if raiz:
        print(f'{raiz.dado} ', end='')
        mostra(raiz.esq)
        print(' ', end='')
        mostra(raiz.dir)

    print(')', end='')