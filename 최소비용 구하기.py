import heapq
import sys

input = sys.stdin.readline

def dijkstra(g, start, end):
    distances = [float('inf')] * len(g)
    distances[start] = 0
    pq = [(0,start)]
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
    return distances
g = [[] for i in range(int(input())+1)]
for i in range(int(input())):
    s,e,m = map(int, input().split())
    g[s].append([e,m])
start, end = map(int, input().split())
distances = dijkstra(g,start, end)
print(distances[end])
