import sys, heapq

input = sys.stdin.readline


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    v1,v2,w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

need1, need2 = map(int, input().split())
def dijkstra(g, start, end):
    distances = [float('inf')] * (n+1)
    distances[start] = 0
    pq = [[0, start]]
    while pq:
        curr_dist, curr_vert = heapq.heappop(pq)
        if curr_dist > distances[curr_vert]:
            continue
        if curr_vert == end:
            break
        for vertex, weight in g[curr_vert]:
            new_dist = curr_dist + weight
            if new_dist < distances[vertex]:
                distances[vertex] = new_dist
                heapq.heappush(pq, (new_dist, vertex))
    return distances[end]


dis1 = dijkstra(graph, 1, need1) + dijkstra(graph, need1, need2) + dijkstra(graph, need2, n)
dis2 = dijkstra(graph, 1, need2) + dijkstra(graph, need2, need1) + dijkstra(graph, need1, n)
if dis1 == dis2 == float('inf'):
    print(-1)
    exit()
print(min(dis1, dis2))