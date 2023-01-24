def minimo(x,y):
    return [x,0] if x<y else [y,1]


num_wookiees = int(input())
fila = list()
lista_sobra = list()
primeiro_da_fila = 0
ja_colocou = False
for i in range (num_wookiees):
    fila.append(list())

lista_de_cargas = input().split()

for a in range(len(lista_de_cargas)):
    lista_de_cargas[a] = int(lista_de_cargas[a])
    
min = minimo(len(fila), len(lista_de_cargas))

for a in range(min[0]): # Adicionar cargas nas listas vazias
        fila[a].insert(0,lista_de_cargas[a])
    
for a in range(min[0]-1,-1,-1):
    lista_de_cargas.pop(a)

for a in range(len(lista_de_cargas)):
    ja_colocou = False
    for b in range(primeiro_da_fila,len(fila)):
        if lista_de_cargas[a] <= fila[b][len(fila[b])-1]:
            fila[b].append(lista_de_cargas[a])
            ja_colocou = True
            primeiro_da_fila = b 
            break
    
    if not ja_colocou:
        lista_sobra.append(lista_de_cargas[a])
        primeiro_da_fila = 0
        
for a in range(len(fila)):
    peso = 0
    for b in fila[a]:
        peso += b
    fila[a].insert(0,peso)

b = len(fila)
while b:
    for a in range(len(fila)-1):
        if fila[a][0] < fila[a+1][0]:
            fila[a],fila[a+1] = fila[a+1],fila[a]
    b-=1

if num_wookiees == 0:
    print('Os Wookies foram para o lado sombrio da força!')
    
for a in range(len(fila)):
    fila[a].pop(0)
    print('%s ' %fila[a], end = '')
    if a == len(fila) - 1:
       print() 

for a in range(len(lista_sobra)):
    print('%d '%lista_sobra[a], end = '')
    if a == len(lista_sobra) - 1:
       print() 
   
if min[1]:
    print('A força está com os Wookies!')