import heapq
import sys

iinput = sys.stdin.readline


def dijkstra(g, start):
    distances = [float('inf')] * len(g)
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        curr_dist, curr_vert = heapq.heappop(pq)
        if curr_dist > distances[curr_vert]:
            continue
        for vertex, weight in g[curr_vert]:
            new_dist = curr_dist + weight
            if new_dist < distances[vertex]:
                distances[vertex] = new_dist
                heapq.heappush(pq, (new_dist, vertex))
    return distances


v, k = map(int, iinput().split())

g = [[] for i in range(v)]
start = int(input())
for i in range(k):
    s, e, m = map(int, iinput().split())
    g[s].append([e, m])
distances = dijkstra(g, start)
for i in range(1,v+1):
    if distances[i] != float('inf'):
        print(distances[i])
    else:
        print('INF')
