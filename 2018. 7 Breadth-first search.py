from collections import deque
N = int(input())
gragh = {}
distances = {}
for i in range(N-1):
    worker,boss = input().split()
    if (worker in gragh) == False:
        gragh[worker] = set()
    if (boss in gragh) == False:
        gragh[boss] = set()
    gragh[boss].add(worker)
    distances[worker] = None
start_vertex = 'X'
distances[start_vertex] = 0
print(distances,gragh)
queue = deque([start_vertex])
while queue:
    cur_v = queue.popleft()
    for neigh_v in gragh[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            queue.append(neigh_v)
for i in distances:
    print(i,distances[i])
