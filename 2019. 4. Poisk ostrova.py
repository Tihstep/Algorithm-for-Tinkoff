def zalifka(opens,point,mask):
    ##print(mask)
    count = 0
    if opens[point[0]][point[1]]=='*':
        return 0
    if mask[point[0]][point[1]] != True:
        return 0
    mask[point[0]][point[1]] = False
    count+=1
    count+= zalifka(opens,[point[0]+1,point[1]],mask)
    count+= zalifka(opens,[point[0]-1,point[1]],mask)
    count+= zalifka(opens,[point[0],point[1]+1],mask)
    count+= zalifka(opens,[point[0],point[1]-1],mask)
    return count

N = int(input())
opens = []
count = 0
mask = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    opens.append(input().split())
for i in range(N):
    for j in range(N):
        if(opens[i][j] == '.'):
            mask[i][j] = True
point = list(map(int,input().split()))
count = zalifka(opens,point,mask)
print(count)
