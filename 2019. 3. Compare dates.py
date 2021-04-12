def perevod(x):
    return 24*60*(x[0]-1) + 60*x[1] + x[2]
def abc(a,b):
    if a > b:
        return a - b
    else: 
        return 10080 + b-a
    
def date_diff(count_near,count,now):
    a,b,c = map(perevod,[count_near,count,now])
    return abc(b,c)>abc(a,c)
        
        
    
    
    
    
now = list(map(int,input().split()))
n = int(input())
matrix = []
count = list(map(int,input().split()))
for _ in range(n-1):
    matrix.append(list(map(int,input().split())))
for i in range(n-1):
    if date_diff(count,matrix[i],now):
        count = matrix[i]
print(" ".join(map(lambda x: "{}".format(x),count)))
