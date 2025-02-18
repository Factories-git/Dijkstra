import heapq


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


def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    for s,e in edge:
        graph[s].append((e, 1))
        graph[e].append((s, 1))
    dis = dijkstra(graph, 1)
    max_ = max(dis[1:])
    for i in range(1, len(dis)):
        if dis[i] == max_:
            answer += 1
    return answer


print(solution(	6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))