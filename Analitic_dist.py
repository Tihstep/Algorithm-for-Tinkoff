N, M, P = input().split()
N, M = int(N), int(M)
P = float(P)

def combinations(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
    for t in range(1, min(k, n - k) + 1):
        nn *= n
        kk *= t
        n -= 1
        return nn // kk
    else:
        return 0

def bernulli(tests, k, m):
    return combinations(tests,k)*((1/m)**k)*((1-1/m)**(tests - k))


def p(max_, tests, m):
    val = 0
    for i in range(max_ + 1):
        val += bernulli(tests, i, m)
    return val


x = 1000
while((1 - p(N, x, M) < P)):
    x += 1000


print(int(x/1000))
