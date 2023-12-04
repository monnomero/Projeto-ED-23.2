import pyautogui
import mouse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
import random
import os

def tupla_para_int(cor_tupla):
    r, g, b = cor_tupla
    rgb_inteiro= r * 256 ** 2 + g * 256 ** 1 + b * 256 ** 0
    return rgb_inteiro

class Cor:
    def __init__(self, red, green, blue):
        self.hex = (red, green, blue)
        self.val = tupla_para_int(self.hex)
        self.red = red
        self.green = green
        self.blue = blue
        self.esquerda = None
        self.direita = None
        self.altura = 1  # Altura inicial

class AVLTree:
    def __init__(self):
        self.root = None

    # Função para obter a altura de um nó
    def altura(self, node):
        if node is None:
            return 0
        return node.altura

    # Função para obter o fator de balanceamentoamento de um nó
    def balanceamento(self, node):
        if node is None:
            return 0
        return self.altura(node.esquerda) - self.altura(node.direita)

    # Função para realizar a rotação à direita em um nó
    def rotacionar_direita(self, z):
        y = z.esquerda

        if y is None:
            return z  

        T3 = y.direita

        if T3 is not None:
            z.esquerda = T3
        else:
            z.esquerda = None

        y.direita = z

        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    # Função para realizar a rotação à esquerda em um nó
    def rotacionar_esquerda(self, z):
        y = z.direita

        if y is None:
            return z  

        T2 = y.esquerda

        if T2 is not None:
            z.direita = T2
        else:
            z.direita = None

        y.esquerda = z

        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y
    
    # Função para inserir um nó na árvore AVL
    def distancia_cores(self, cor1, cor2):
        r1, g1, b1 = cor1
        r2, g2, b2 = cor2
        return np.sqrt((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2)

    def iserir(self, node, hex_tuple):
        red, green, blue = hex_tuple
        int_val = tupla_para_int((red, green, blue))  

        if node is None:
            return Cor(red, green, blue)

        cor_atual = (node.red, node.green, node.blue)
        similaridade = self.distancia_cores(cor_atual, (red, green, blue))

        if similaridade < 30:  # Medida 2 de avaliação, a partir da "distância" dos valores rgb
            node.esquerda = self.iserir(node.esquerda, hex_tuple)
        else:
            # Se não são similares, faz do jeito normal comparando seu valor inteiro
            if int_val < node.val:
                node.esquerda = self.iserir(node.esquerda, hex_tuple)
            elif int_val > node.val:
                node.direita = self.iserir(node.direita, hex_tuple)
            else:
                pass

        node.altura = 1 + max(self.altura(node.esquerda), self.altura(node.direita))
        balanceamento = self.balanceamento(node)

        # Casos de rotação
        if balanceamento > 1:
            if tupla_para_int((red, green, blue)) > node.esquerda.val:
                return self.rotacionar_direita(node)
            if tupla_para_int((red, green, blue)) < node.esquerda.val:
                node.esquerda = self.rotacionar_esquerda(node.esquerda)
                return self.rotacionar_direita(node)

        if balanceamento < -1:
            if tupla_para_int((red, green, blue)) < node.direita.val:
                return self.rotacionar_esquerda(node)
            if tupla_para_int((red, green, blue)) > node.direita.val:
                node.direita = self.rotacionar_direita(node.direita)
                return self.rotacionar_esquerda(node)

        return node
    
    def pegar_menor_valor(self, node):
        atual = node
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def deletar(self, root, hex_tuple):
        if root is None:
            return root

        int_val = tupla_para_int(hex_tuple)
        if int_val < root.val:
            root.esquerda = self.deletar(root.esquerda, hex_tuple)
        elif int_val > root.val:
            root.direita = self.deletar(root.direita, hex_tuple)
        else:
            if root.esquerda is None:
                temp = root.direita
                root = None
                return temp
            elif root.direita is None:
                temp = root.esquerda
                root = None
                return temp

            temp = self.pegar_menor_valor(root.direita)
            root.val = temp.val
            root.direita = self.deletar(root.direita, temp.hex)

        if root is None:
            return root

        root.altura = 1 + max(self.altura(root.esquerda), self.altura(root.direita))
        balanceamento = self.balanceamento(root)

        # Casos de rotação
        if balanceamento > 1:
            if tupla_para_int(hex_tuple) > root.esquerda.val:
                return self.rotacionar_direita(root)
            if tupla_para_int(hex_tuple) < root.esquerda.val:
                root.esquerda = self.rotacionar_esquerda(root.esquerda)
                return self.rotacionar_direita(root)

        if balanceamento < -1:
            if tupla_para_int(hex_tuple) < root.direita.val:
                return self.rotacionar_esquerda(root)
            if tupla_para_int(hex_tuple) > root.direita.val:
                root.direita = self.rotacionar_direita(root.direita)
                return self.rotacionar_esquerda(root)

        return root
    
    # Função para encontrar uma cor na árvore AVL
    def busca(self, node, hex_tuple):
        red, green, blue = hex_tuple
        if node is None or node.val == tupla_para_int((red, green, blue)):
            return node

        if tupla_para_int((red, green, blue)) < node.val:
            return self.busca(node.esquerda, (red, green, blue))
        else:
            return self.busca(node.direita, (red, green, blue))
        
    def inorder(self, node, lista_inorder,printar):
        if node is not None:
            self.inorder(node.esquerda, lista_inorder,printar)
            if printar == True:
                print(f"RGB: {node.red}, {node.green}, {node.blue}")
            lista_inorder.append(node.hex)
            self.inorder(node.direita, lista_inorder,printar)
    
    def pegar_cores(self, node):
        cores = []
        if node is not None:
            cores.extend(self.pegar_cores(node.esquerda))
            cores.extend(self.pegar_cores(node.direita))
            cores.append((node.red, node.green, node.blue))
        return cores

    # Função para plotar cores em um gradiente
    def plot_gradiente(self):
        cores = self.pegar_cores(self.root)
        cores.sort()  

        plt.figure(figsize=(10, 1))
        plt.imshow([cores], aspect='auto')
        plt.axis('off')
        plt.title('Gradiente de Cores')
        plt.show()


def selecionar_com_mouse(limitado):
    terminou=False
    lista = []
    lista_inorder = []
    avl_tree.inorder(avl_tree.root, lista_inorder,False)
    valor_inicial = len(lista_inorder)
    
    while True:
        time.sleep(0.050)

        if mouse.is_pressed("left"):
            while True:            
                # Pegar posicao do mouse e cor do pixel
                x, y = pyautogui.position()
                px = pyautogui.pixel(x, y)
                

                if px not in lista:
                    avl_tree.root=avl_tree.iserir(avl_tree.root,px)
                    print(px)
                    lista.append(px)
                    if limitado:
                        if len(lista)== 4**(n+3)-valor_inicial:
                            terminou=True
                            break
                if mouse.is_pressed("right"):
                    terminou = True
                    break
        if terminou==True:
            break

def animar_cores(cores):
    fig, ax = plt.subplots(figsize=(3, 3))  
    plt.axis('off')
    ims = []
    for cor in cores:
        im = ax.imshow([[cor]], animated=True)
        ims.append([im])

    def update(frame):
        ax.clear()
        ax.imshow([[cores[frame]]])
        ax.set_title(f"RGB: {cores[frame]}")
    
    ani = FuncAnimation(fig, update, frames=len(cores), interval=50, repeat=False)
    plt.show()
    
def plot_arte(lista_inorder):
    lista_length = len(lista_inorder)
    grid_tamanho = int(np.sqrt(lista_length))
    num_mini_grids = 4
    mini_grid_tamanho = int(grid_tamanho // np.sqrt(num_mini_grids))

    batch_tamanho = 4**(n+2)
    lista_embaralhada = []

    for i in range(0, len(lista_inorder), batch_tamanho):
        batch = lista_inorder[i:i + batch_tamanho]
        random.shuffle(batch)
        lista_embaralhada.extend(batch)
    lista_inorder=lista_embaralhada

    mini_grids = np.zeros((mini_grid_tamanho, mini_grid_tamanho, num_mini_grids), dtype=np.uint8)
    art = np.zeros((grid_tamanho, grid_tamanho, 3), dtype=np.uint8)
    cont=0
    for i in range(num_mini_grids): 
        mini_grids[:, :, i] = np.random.randint(i * mini_grid_tamanho**2, (i + 1) * mini_grid_tamanho**2,
                                                size=(mini_grid_tamanho, mini_grid_tamanho))
        for j in range(mini_grid_tamanho):
            for k in range(mini_grid_tamanho):
                cor_index = cont
                if i < 2: 
                    art[ k,mini_grid_tamanho *i+ j] = lista_inorder[cor_index]
                else:
                    art[mini_grid_tamanho + k, mini_grid_tamanho * (i - 4) + j] = lista_inorder[cor_index]
                cont+=1
    #Mostrar a arte gerada
    plt.figure(figsize=(8, 8))
    plt.imshow(art)
    plt.axis('off')
    plt.title('Arte Abstrata')
    plt.show()
    
comando = "começo"
avl_tree = AVLTree()
while comando != "FIM":
    print("O que você quer fazer?")
    print("Opções: Inserir cores manualmente (ICM), Inserir cores com o mouse (ICCM), Buscar cor na árvore: (B), Deletar cor na árvore (D), Printar a travessia inorder (PTI), Plotar o gradientee das cores (PG), Plotar a animação das cores em inorder (PA), Plotar uma arte abstrata ao adicionar cores à arvore até uma potência de 4 (PAA), Limpar o terminal (C), Resetar a árvore: (R), Finalizar o programa (FIM)")
    comando = input("Digite a opção das presentes em parênteses: ")
    
    if comando == "ICM":
        cor = input("Qual cor deseja inserir? Digite-a na forma 255,255,255: ").split(",")
        cor_int = [0,0,0]
        for elemento in range(3):
            cor_int[elemento] = int(cor[elemento]) 
        cor_int = tuple(cor_int)
        avl_tree.root=avl_tree.iserir(avl_tree.root,cor_int)
        
    elif comando == "ICCM":
        print("A partir do momento que você apertar com o botão esquerdo, as cores que seu ponteiro aponta serão adicionadas à arvore. Para parar, clique com o botão direito")
        selecionar_com_mouse(False)
        
    elif comando == "B":
        cor = input("Qual cor deseja inserir? Digite-a na forma 255,255,255: ").split(",")
        cor_int = [0,0,0]
        for elemento in range(3):
            cor_int[elemento] = int(cor[elemento]) 
        cor_int = tuple(cor_int)
        resultado = avl_tree.busca(avl_tree.root, cor_int)
        if resultado is not None:
            print("Cor achada na árvore!")
        else:
            print("Cor não está na árvore.")
            
    elif comando == "D":
        cor = input("Qual cor deseja inserir? Digite-a na forma 255,255,255: ").split(",")
        cor_int = [0,0,0]
        for elemento in range(3):
            cor_int[elemento] = int(cor[elemento]) 
        cor_int = tuple(cor_int)
        avl_tree.root=avl_tree.deletar(avl_tree.root,cor_int)
        
    elif comando == "PG":
        avl_tree.plot_gradiente()
        
    elif comando == "PA":
        lista_inorder = []
        avl_tree.inorder(avl_tree.root, lista_inorder,False)
        animar_cores(lista_inorder)
        
    elif comando == "PAA":
        metodo = input("Você quer adicionar novas cores com o mouse (M) ou aleatoriamente (A)?")
        if metodo == "A":
            n = int(input("Selecione um numero de 1 a 4 para o numero de cores necessarias para fazer a arte, sendo que 1 = 256 cores, 2 = 1024, 3 = 4096, N° cores = 4**(n+3): "))
            if n<1 or n>4:
                n=2
            lista_inorder = []
            avl_tree.inorder(avl_tree.root, lista_inorder,False)
            valor_inicial = len(lista_inorder)
            cores_aleatorias = np.random.randint(0,256,size=(4**(n+3)-valor_inicial,3))
            for cor in cores_aleatorias:
                avl_tree.root=avl_tree.iserir(avl_tree.root,cor)
            lista_inorder = []
            avl_tree.inorder(avl_tree.root, lista_inorder,False)
            plot_arte(lista_inorder)
        elif metodo == "M":
            n = int(input("Selecione um numero de 1 a 4 para o numero de cores necessarias para fazer a arte, sendo que 1 = 256 cores, 2 = 1024, 3 = 4096, N° cores = 4**(n+3): "))
            if n<1 or n>4:
                n=1
            selecionar_com_mouse(True)
            lista_inorder = []
            avl_tree.inorder(avl_tree.root, lista_inorder,False)
            plot_arte(lista_inorder)
            
    elif comando == "PTI":
        lista_inorder=[]
        avl_tree.inorder(avl_tree.root, lista_inorder,True)
        
    elif comando == "C":
        os.system('cls' if os.name == 'nt' else 'clear')
    
    elif comando == "R":
        avl_tree = AVLTree()  
        
    elif comando == "fim":
        break
    print()