import Node

class CriateTree(object):

    def __init__(self):
        estado = self.estado_inicial()
        self.root = Node.Node(estado,9)
        self.completar_arvore(self.root, 9, 0)
        return None

    def completar_arvore(self, nodo, profundidade, x):
        if profundidade == 0:
            return None
        else:
            novo = self.copia(nodo.estado)
            if (profundidade % 2) == 0:
                self.marcar(novo,'O', x)
                nodo.filhos[x] = Node.Node(novo,profundidade-1)
                self.completar_arvore(nodo.filhos[x], profundidade - 1, x)
                if x < profundidade:
                    self.completar_arvore(nodo.filhos[x], profundidade-1,x)
            else:
                self.marcar(novo,'X', x)
                nodo.filhos[x] = Node.Node(novo, profundidade-1)
                self.completar_arvore(nodo.filhos[x],profundidade -1, x)
                if x < profundidade:
                    self.completar_arvore(nodo.filhos[x], profundidade-1,x)
        return None


    # def completar_arvore(self, node):
    #     aux  = []
    #     aux.append(node)
    #     for i in range(0, aux[0].profundidade):
    #         novo = self.copia(aux[0].estado)
    #         self.marcar(novo,'X',i)
    #         aux[0].filhos[i] = Node.Node(novo, aux[0].profundidade-1)
    #         aux.append(aux[0].filhos[i])
    #         for j in range(0, aux[1].profundidade):
    #             novo = self.copia(aux[1].estado)
    #             self.marcar(novo, 'O', j)
    #             aux[1].filhos[j] = Node.Node(novo, aux[1].profundidade-1)
    #             aux.append(aux[1].filhos[j])
    #             for k in range(0, aux[2].profundidade):
    #                 novo = self.copia(aux[2].estado)
    #                 self.marcar(novo, 'X', k)
    #                 aux[2].filhos[k] = Node.Node(novo, aux[2].profundidade-1)
    #                 aux.append(aux[2].filhos[k])
    #                 for l in range(0, aux[3].profundidade):
    #                     novo = self.copia(aux[3].estado)
    #                     self.marcar(novo, 'O', l)
    #                     aux[3].filhos[l] = Node.Node(novo, aux[3].profundidade-1)
    #                     aux.append(aux[3].filhos[l])
    #                     for m in range(0, aux[4].profundidade):
    #                         novo = self.copia(aux[1].estado)
    #                         self.marcar(novo, 'X', m)
    #                         aux[4].filhos[m] = Node.Node(novo, aux[4].profundidade-1)
    #                         aux.append(aux[4].filhos[m])
    #                         for n in range(0, aux[5].profundidade):
    #                             novo = self.copia(aux[5].estado)
    #                             self.marcar(novo, 'O', n)
    #                             aux[5].filhos[n] = Node.Node(novo, aux[5].profundidade-1)
    #                             aux.append(aux[5].filhos[n])
    #                             for o in range(0, aux[6].profundidade):
    #                                 novo = self.copia(aux[6].estado)
    #                                 self.marcar(novo, 'X', o)
    #                                 aux[6].filhos[o] = Node.Node(novo, aux[6].profundidade-1)
    #                                 aux.append(aux[6].filhos[o])
    #                                 for p in range(0, aux[7].profundidade):
    #                                     novo = self.copia(aux[7].estado)
    #                                     self.marcar(novo, 'O', p)
    #                                     aux[7].filhos[p] = Node.Node(novo, aux[7].profundidade-1)
    #                                     aux.append(aux[7].filhos[p])
    #                                     for q in range(0, aux[8].profundidade):
    #                                         novo = self.copia(aux[1].estado)
    #                                         self.marcar(novo, 'X', q)
    #                                         aux[8].filhos[q] = Node.Node(novo, aux[8].profundidade-1)
    #                                         aux.append(aux[8].filhos[q])


    def estado_inicial(self):
        estado = [['_','_','_'],
                  ['_','_','_'],
                  ['_','_','_']]
        return estado

    def copia(self, estado):
        novo = [[0,0,0],
                [0,0,0],
                [0,0,0]]
        for i in range(0,3):
            for j in range(0,3):
                novo[i][j] = estado[i][j]
        return novo

    def marcar(self, estado, jogador, i):
        x = 0
        y = 0
        z = 0

        while x != i:
            if estado[y][z] == '_':
                x += 1
            z += 1
            if z == 3:
                y += 1
                z = 0
        while y < 3:
            if estado[y][z] == '_':
                estado[y][z] = jogador
                break
            z += 1
            if z == 3:
                y += 1
                z = 0