class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Importante lembrar das aulas de estrutura de dados, porém transcrevendo de Java para Python
#Prefixo = Raiz -> Esquerda -> Direita
#Infixo = Esquerda -> Raiz -> Direita
#Posfixo = Esquerda -> Direita -> Raiz

def inserir(root, value):
    if root is None:
        return No(value)
     
    if value<root.value:
        root.left = inserir(root.left, value)
    else:
        root.right = inserir(root.right, value)
    
    return root

def preorder(root, resultado):
    if root:
        resultado.append(root.value)
        preorder(root.left, resultado)
        preorder(root.right, resultado)

def inorder(root, resultado):
    if root:
        inorder(root.left, resultado)
        resultado.append(root.value)
        inorder(root.right, resultado)

def postorder(root, resultado):
    if root:
        postorder(root.left, resultado)
        postorder(root.right, resultado)
        resultado.append(root.value)

C = int(input())

for i in range(1, C+1):
    N = int(input())

    valores = list(map(int, input().split()))

    root = None

    for valor in valores:
        root = inserir(root, valor)

    prefixo = []
    infixo = []
    posfixo = []

    preorder(root, prefixo)
    inorder(root, infixo)
    postorder(root, posfixo)

    print(f'Case {i}:')
    print("Pre.:", " ".join(map(str, prefixo)))
    print("In..:", " ".join(map(str, infixo)))
    print("Post:", " ".join(map(str, posfixo)))
    print()
