class Node(object):

    def __init__(self, estado=None, profundidade=None):
        self.profundidade = profundidade
        self.estado = estado
        self.filhos = []
        for i in range(0, profundidade):
            self.filhos.append(None)
