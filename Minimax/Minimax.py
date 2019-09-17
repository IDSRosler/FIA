import Node

class Minimax(object):

    def completar_arvore(self, nodo, profundidade):
        if profundidade == 0:
            return None
        else:
            lista = nodo.filhos
            for i in range(0,len(lista)):
                novo = self.copiar(nodo.estado)
                if (profundidade % 2) == 0:
                    self.marcar(novo,'O', i)
                    alpha = self.verificar(novo)
                    if alpha == 0:
                        nodo.filhos[i] = Node.Node(novo,profundidade-1)
                        self.completar_arvore(nodo.filhos[i], profundidade - 1)
                    else:
                        nodo.filhos[i] = Node.Node(novo, 0)
                else:
                    self.marcar(novo,'X', i)
                    alpha = self.verificar(novo)
                    if alpha == 0:
                        nodo.filhos[i] = Node.Node(novo, profundidade - 1)
                        self.completar_arvore(nodo.filhos[i], profundidade - 1)
                    else:
                        nodo.filhos[i] = Node.Node(novo, 0)

    def minimax(self, nodo, profundidade, maximizador):
        if nodo.profundidade == 1:
            return self.verificar(nodo.estado)
        elif maximizador == False:
            alpha = 3
            lista = nodo.filhos
            for filho in lista:
                alpha = min(alpha, self.minimax(filho, profundidade - 1, True))
            return alpha
        else:
            alpha = -3
            lista = nodo.filhos
            for filho in lista:
                alpha = max(alpha, self.minimax(filho, profundidade - 1, False))
            return alpha

    def cont_estados(self, nodo, profundidade, cont = 0):
        if profundidade == 0:
            return 1
        else:
            lista = nodo.filhos
            for filho in lista:
                cont += self.cont_estados(filho, profundidade - 1)
        return cont

    def copiar(self, estado):
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

    def verificar(self, estado):
        #Checar linhas
        for i in range(0,3):
            if (estado[i][0] == estado[i][1] == estado[i][2]) and estado[i][0] != '_':
                if estado[i][0] == 'X':
                    return 1
                else:
                    return -1
        #Checar colunas
        for j in range(0,3):
            if (estado[0][j] == estado[1][j] == estado[2][j]) and estado[0][j] != '_':
                if estado[0][j] == 'X':
                    return 1
                else:
                    return -1
        #Checar diagonais
            if ((estado[0][0] == estado[1][1] == estado[2][2]) or (estado[0][2] == estado[1][1] == estado[2][0])) and estado[1][1] != '_':
                if estado[0][0] == 'X':
                    return 1
                else:
                    return -1
        return 0