def le_filhos(raiz, filhos):
    if filhos:
        entrada = input().split()
        dados = entrada[::2]
        num_filhos = entrada[1::2]

        raiz.filhos = [Arvore(d) for d in dados]
        for i in range(filhos):
            le_filhos(raiz.filhos[i], int(num_filhos[i]))


def leia():
    dado, filhos = input().split()
    raiz = Arvore(dado)
    le_filhos(raiz, int(filhos))

    return raiz