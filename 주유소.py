import heapq


def dijkstra(g, start):
    re = [0] * n
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
                print(curr_dist, curr_vert)
    return distances[-1]


n, m = map(int, input().split())
g = [[] * n for _ in range(m)]
oils = []
money = list(map(int, input().split()))
for i in range(m):
    f, s, l = map(int, input().split())
    g[f - 1].append((s - 1, l))
    g[s - 1].append((f - 1, l))
start = 0
target = n - 1
distances = dijkstra(g, start)
print(distances)
