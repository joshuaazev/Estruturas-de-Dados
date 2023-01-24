class ABB():
    def __init__(self, dado=None, esq=None, dir=None):
        self.dado = dado
        self.esq = esq
        self.dir = dir

    def __str__(self):
        if self.dado is None:
            return '()'

        esq = self.esq if self.esq else '()'
        dir = self.dir if self.dir else '()'
        return f'({self.dado} {esq} {dir})'
        
    
    def add(self, dado):
        if self.dado is None:
            self.dado = dado
        elif self.dado < dado:
            if not self.dir:
                self.dir = ABB()
            self.dir.add(dado)
        else:
            if not self.esq:
                self.esq = ABB()
            self.esq.add(dado)

raiz = ABB()
n = int(input())
if n > 0:
    for dado in input().split():
        raiz.add(int(dado))

print(raiz)