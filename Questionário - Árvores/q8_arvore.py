N = int(input())

for _ in range(N):
    esq, dir = (0, 1), (1, 0)
    atual = (1, 1)
    for direção in input():
        if direção == 'E':
            atual, dir = (esq[0] + atual[0], esq[1] + atual[1]), atual
        else:
            esq, atual = atual, (dir[0] + atual[0], dir[1] + atual[1])
    print(f'{atual[0]} / {atual[1]}')