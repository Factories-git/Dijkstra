import heapq


def dijkstra(g, start):
    distances = [float('inf')] * len(g)
    distances[start] = 0
    pq = [(0, start)]
    previous = [None] * len(g)
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
                previous[vertex] = curr_vert #과거에 최단경로로 가기 위해서 이 노드를 방문했음.
                heapq.heappush(pq, (new_dist, vertex))

    path = []
    current = end #0이 될때까지 계속 현재 노드를 바꿈
    while current:
        path.append(current) #최단경로로 가기 위해서 길을 지났음.
        current = previous[current] #그 노드로 이동해서 또 다른 노드(최단경로로 가기 위해서 거치는 노드)를 찾음.
    # path는 뒤집어서 반영되기 때문에 (역추적) 뒤집어서 반환.
    return path[::-1], distances


n = int(input())
m = int(input())
g = [[] for i in range(n + 1)]
for i in range(m):
    s, e, w = map(int, input().split())
    g[s].append((e, w))
start, end = map(int, input().split())
path, dis = dijkstra(g, start)
print(dis[end])
print(len(path))
print(*path)
