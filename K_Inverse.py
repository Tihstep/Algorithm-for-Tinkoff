def add(t,i,a):
    while(i <= n):
        A[t][i] = (A[t][i] + a) % mod 
        i += i & -i
        
        
def suma(t, i):
    sum_ = 0
    while(i>0):
        sum_ = (sum_ + A[t][i]) % mod
        i -= i & -i
    return sum_
        
        
mod = 1000000000
A = []
for i in range(11):
    A.append([0] * 20001)
n, k = map(int, input().split())
input_seq = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    x = input_seq[i]
    add(1, x, 1)
    for l in range(1,k):
        add(l+1, x, suma(l, x-1))
print(suma(k,n))
