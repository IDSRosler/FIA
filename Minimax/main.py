import Minimax
import Node

estado_inicial = [['_','_','_'],
                  ['_','_','_'],
                  ['_','_','_']]
cont = 0

minimax = Minimax.Minimax()
root = Node.Node(estado_inicial,9)
minimax.completar_arvore(root,9)
resultado_minimax = minimax.minimax(root,9,True)
print("O resultado minimax da raiz do jogo da velha é: {}".format(resultado_minimax))
cont = minimax.cont_estados(root,9)
print("Quantidade de estados existentes: {}".format(cont))