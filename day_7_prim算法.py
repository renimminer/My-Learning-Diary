def prim(graph, vertex_num):
    INF = 1 << 10
    visit = [False] * vertex_num
    dist = [INF] * vertex_num
    preIndex = [0] * vertex_num

    for i in range(vertex_num):

        minDist = INF + 1
        nextIndex = -1

        for j in range(vertex_num):
            if dist[j] < minDist and not visit[j]:
                minDist = dist[j]
                nextIndex = j

        print
        nextIndex
        visit[nextIndex] = True

        for j in range(vertex_num):
            if dist[j] > graph[nextIndex][j] and not visit[j]:
                dist[j] = graph[nextIndex][j]
                preIndex[j] = nextIndex

    return dist, preIndex


_ = 1 << 10

graph = [
    [0, 6, 3, _, _, _],
    [6, 0, 2, 5, _, _],
    [3, 2, 0, 3, 4, _],
    [_, 5, 3, 0, 2, 3],
    [_, _, 4, 2, 0, 5],
    [_, _, _, 3, 5, 0],
]

print(prim(graph, 6))
