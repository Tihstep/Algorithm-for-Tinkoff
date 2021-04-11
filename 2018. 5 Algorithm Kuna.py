import numpy as np

def dfs(v,used,matching,g):
    if used[v] == True:
        return False
    used[v] = True
    for to in range(len(g[v])):
        if(g[v][to]!=0):
            if((matching[to] == -1) or (dfs(matching[to],used,matching,g))):
                matching[to] = v
                return True
            return False

def kun():
    g = []
    n,m = list(map(int,input().split()))
    matching = [-1]*m
    used = [False]*n
    for i in range(m):
        current = list(map(int,input().split()))
        g.append(current)
    g = np.array(g).T
    for i in range(n):
        dfs(i,used,matching,g)
    print(matching)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
