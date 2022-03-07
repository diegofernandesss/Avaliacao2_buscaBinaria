class Vertice:
    def __init__(self, key, payload):
        self.key    = int(key)
        self.payload= payload
        self.pai    = None
        self.left   = None
        self.right  = None
      
    def __str__(self):
        return str(self.key)+" ==> "+\
            str(self.payload) 

class Tree:
    def __init__(self):
        self.raiz = None
        self.count= 0

    def treeInsert(self, z):
        y = None # y começa apontando para o pai da raiz (None)
        x = self.raiz # x eh usado para detectar o vertice pai do adicionado

        while(x != None):
            y = x
            if(z.key < x.key):
                x = x.left
            else:
                x = x.right
        z.pai = y
        if(y == None):
            self.raiz = z
        elif(z.key < y.key):
            y.left = z
        else:
            y.right = z
        self.count += 1

    def iteractive_tree_search(self, key):
        if(self.raiz == None):
            return None
            
        vertice = self.raiz
        while(vertice != None and vertice.key != int(key)):
            if(int(key) < vertice.key):
                vertice = vertice.left
            else:
                vertice = vertice.right
        
        return vertice
    
    def inorder_tree_walk(self, vertice=None):
        if(self.raiz == None): # Para o caso de uma árvore vazia
            return None
        
        if(vertice == None):    # Para o primeiro nível da árvore de recursão
            vertice = self.raiz
        
        if(vertice.left != None): # Condição de parada. Vértice esquerdo == None
            self.inorder_tree_walk(vertice=vertice.left)    # Decomposição do problema em uma
                                                            # versão menor

        print(vertice)
        
        if(vertice.right != None): # Condição de parada. Vértice direito == None
            self.inorder_tree_walk(vertice=vertice.right)   # Decomposição do problema em uma 
                                                            # versão menor

    def pre_order(self, vertice=None):
        if(self.raiz == None):
            return 
        if(vertice == None):
            vertice = self.raiz
        print(vertice)
        if(vertice.left != None):
            self.pre_order(vertice=vertice.left)
        if(vertice.right != None):
            self.pre_order(vertice=vertice.right)
        

    def pos_order(self, vertice=None):
        if(self.raiz == None):
            return 
        if(vertice == None):
            vertice = self.raiz
        if(vertice.left != None):
            self.pos_order(vertice=vertice.left)
        if(vertice.right != None):
            self.pos_order(vertice=vertice.right)
        print(vertice)


    def tree_minimum(self, vertice = None):
        if(self.raiz == None):
            return None

        if(vertice == None):
            vertice = self.raiz

        while(vertice.left != None):
            vertice = vertice.left

        return vertice
    
    def print_decrescente(self, vertice=None):
        if (self.raiz == None):
            return 
        if (vertice == None):
            vertice = self.raiz
        if (vertice.right != None):
          self.print_decrescente(vertice=vertice.right)
        print(vertice)
        if (vertice.left != None):
          vertice = self.print_decrescente(vertice=vertice.left)

    def tree_minimum_recursivo(self, vertice=None):
        if(self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        if (vertice.left != None):
            vertice = self.tree_minimum_recursivo(vertice=vertice.left)
        return vertice

    def tree_sucessor(self, vertice):
        # caso 1 - Possui a subárvore direita
        if(vertice.right != None):
            return self.tree_minimum(vertice = vertice.right)

        # Caso 2 - Não possui a subárvore direita
        y = vertice.pai
        while(y != None and vertice == y.right):
            vertice = y
            y = vertice.pai
        return y
    
    def tree_maximum(self, vertice=None):
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        while (vertice.right != None):
            vertice = vertice.right
        return vertice


    def tree_predecessor(self, vertice=None):
        if(vertice.left != None):
            return self.tree_maximum(vertice=vertice.left)
        y = vertice.pai
        while (y != None and vertice == y.left):
            vertice = y
            y = vertice.pai
        return y

    def tree_transplant(self, u, v):
        # caso 1
        if(u.pai == None):
            self.raiz = v
        elif(u.pai.left == u): #caso 2
            u.pai.left = v
        else:
            u.pai.right = v

        if(v != None):      # Pai de u vira o pai
            v.pai = u.pai   # de v em todos os casos

    # Remove um vértice da árvore
    # A dificuldade dessa operaão é encontrar um novo pai de família para os filhos do
    # vértice removido
    def tree_remove(self, z): # Três casos possíveis
        if(z.left == None): # Não possui a subárvore esquerda, então o filho direito será
            self.tree_transplant(z, z.right)# o novo pai da família de z que foi removido
        elif(z.right == None): # Não possui a subárvore direita, então o filho esquerdo será
            self.tree_transplant(z, z.left)# o novo pai da família de z que foi removido
        else: # Tem as duas subárvores
            y = self.tree_minimum(z.right) # Encontra o vértice de menor chave na subárvore
            # direita (o mínimo não tem os filhos esquerdos)
            if(y.pai != z): # Se y não for filho de z, trnasplante a subárvore direita de y
                # para a posição de y
                self.tree_transplant(y, y.right)
                y.right = z.right # Já ajusta os filhos direitos de y para ser a subárvore
                y.right.pai = y   # direita de z

            self.tree_transplant(z, y) # Faça o transplant de y para a posição de z
            y.left = z.left
            y.left.pai = y
    
    def tree_remove_maximum(self, z):
        if (z.right == None):
            self.tree_transplant(z, z.left)
        elif (z.left == None):
            self.tree_transplant(z, z.right)
        else:
            y = self.tree_maximum(z.left)
            if (y.pai != z):
                self.tree_transplant(y, y.left)
                y.left = z.left
                y.left.pai = y
            self.tree_transplant(z, y)
            y.right = z.right
            y.right.pai = y

arvore = Tree()
while(True):
    print("............>MENU<.............")
    print("\033[1;36m(1)-Adiciona vertice")
    print("(2)-Procura vertice")
    print("(3)-Remove vertice")
    print("(4)-Imprime a árvore inorder")
    print("(5)-Sair do programa")
    print("(6)-Imprime o tree predecessor")
    print("(7)-Imprime o Minimum com algoritmo recursivo")
    print("(8)-Imprime o Tree Maximum")
    print("(9)-Imprime o print Decrescente")
    print("(10)-Imprime o tree Pré-Order")
    print("(11)-Imprime o tree Pós-Order")
    print("(12)-Imprime o tree Remove usando o tree_maximum ao invés de tree minimum")
    print("(13)-Imprime o tree Sucessor \033[m")
    print("..............................")
    print("Escolha uma opção:", end="")
    op = int(input())
    if(op==1):
        print("Informe a chave:", end="")
        key = int(input())
        print("Informe o payload:", end="")
        payload = input()
        v = Vertice(key, payload)
        arvore.treeInsert(v)
    elif(op==2):
        print("Informe a chave:", end="")
        key = int(input())
        z = arvore.iteractive_tree_search(key)
        if(z!=None):
            print(z)
        else:
            print(f'\033[0;31m Vertice {key} não está presente na árvore \033[m')
    elif(op==3):
        print("Informe a chave:", end="")
        key = int(input())
        z = arvore.iteractive_tree_search(key)
        if(z!=None):
            arvore.tree_remove(z)
        else:
            print("\033[0;31m Vertice ",key,"não está presente na árvore\033[m")
    elif(op==4):
        print("Arvore inorder_tree_walk")
        arvore.inorder_tree_walk()
      
    elif(op==5):
        print("\033[0;33m \nSaindo do terminal\n\033[m")
        exit(1)

    elif(op==6):
        chave = int(input("Informe a chave:"))
        vertice = arvore.iteractive_tree_search(chave)
        if(vertice == None):
          print(f'\033[0;31mkey {chave} não encontrada\033[m')
        else:
          print(f'predecessor da key : \n {arvore.tree_predecessor(vertice)}')

    elif(op==7):
      print(f'Menor elemento recursivo: \n {arvore.tree_minimum_recursivo()}')

    elif(op==8):
      print(f'Maior elemento key:\n {arvore.tree_maximum()}')

    elif(op==9):
      arvore.print_decrescente()

    elif(op==10):
      arvore.pre_order()

    elif(op==11):
      arvore.pos_order()

    elif(op==12):
      chave = int(input("Informe a chave: "))
      vertice = arvore.iteractive_tree_search(chave)
      if(vertice == None):
        print(f'\033[0;31m key {chave} não encontrada na árvore\033[m')
      else:
        arvore.tree_remove_maximum(vertice)
        print(f'Removido. Por favor verificar na opção 4 no inorder')

    elif(op==13):
      chave = int(input("Informe a chave: "))
      vertice = arvore.iteractive_tree_search(chave)
      if (vertice == None):
        print(f'\033[0;31m key {chave} não encontrada \033[m')
      else:
        print(f'O sucessor da chave são: \n{arvore.tree_sucessor(vertice)}')
  
    else:
      print("\033[0;31mOpção Inválida \033[m")