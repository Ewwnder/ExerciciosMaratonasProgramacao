import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0]*N

    def find(self, X): #Estudar mais esse conceito de encurtar e fazer todos apontarem para a raíz.
        while X!=self.parent[X]:
            self.parent[X] = self.parent[self.parent[X]]
            X = self.parent[X]
        return X
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False
        
        if self.rank[rootA]<self.rank[rootB]:
            self.parent[rootA] = rootB
        else:
            self.parent[rootB] = rootA

            if self.rank[rootA] == self.rank[rootB]:
                self.rank[rootA] += 1
        
        return True

while True:
    M, N = map(int, input().split())

    if M==0 and N==0:
        break

    edges = []
    custo_total = 0

    for _ in range(N):
        x, y, z = map(int, input().split())
        edges.append((z,x,y))
        custo_total+=z

    edges.sort()

    dsu = DSU(M)
    custo_reduzido = 0

    for custo, u, v in edges:
        if dsu.union(u, v):
            custo_reduzido+=custo

    print(custo_total-custo_reduzido)