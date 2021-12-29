'''
Dijkstra's shortest path algorithm
https://labuladong.github.io/algo/2/19/41/
https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/
'''
# path [from, to, distance]
import heapq
from collections import defaultdict
path = [
    [0, 1, 5],
    [0, 2, 8],
    [1, 3, 2],
    [1, 2, 9],
    [1, 0, 5],
    [2, 0, 8],
    [2, 1, 9],
    [2, 3, 6],
    [3, 1, 2],
    [3, 2, 6]
]
# Dijkstra's shortest path algorithm is O(ElgV) where:
# V is the number of vertices
# E is the total number of edges

# Time: O(E+VlgV)
# Space: O(V+E)

# original


# def dijkstra(path: list, n: int, start: int, destination: int) -> int:
#     dist = [float('inf')] * n
#     dist[start] = 0  # for each node, shortest distance from start
#     weight = defaultdict(dict)
#     # create_graph
#     for cur, nxt, d in path:
#         weight[cur][nxt] = d
#         weight[nxt][cur] = d
#     pq = [(0, start)]  # [(dist from start to node, node)]
#     heapq.heapify(pq)
#     while pq:
#         cur_dist, cur_node = heapq.heappop(pq)
#         if cur_node == destination:
#             return cur_dist
#         if dist[cur_node] < cur_dist:
#             continue
#         for nxt_node, nxt_dist in weight[cur_node].items():
#             dist_to_next_node = cur_dist + nxt_dist
#             if dist_to_next_node < dist[nxt_node]:
#                 heapq.heappush(pq, (dist_to_next_node, nxt_node))
#                 dist[nxt_node] = dist_to_next_node
#     return -1

# Improvement
# def dijkstra(path: list, n: int, start: int, destination: int) -> int:
#     dist = [float('inf')] * n
#     weight = defaultdict(dict)
#     # create_graph
#     for cur, nxt, d in path:
#     weight[cur][nxt] = weight[nxt][cur] = d
#         weight[nxt][cur] = d
#     pq = [(0, start)]  # [(dist from start to node, node)]
#     heapq.heapify(pq)
#     while pq:
#         cur_dist, cur_node = heapq.heappop(pq)
#         if cur_node == destination:
#             return cur_dist
#         if cur_dist < dist[cur_node]:
#             dist[cur_node] = cur_dist
#             for nxt_node, nxt_dist in weight[cur_node].items():
#                 heapq.heappush(pq, (cur_dist + nxt_dist, nxt_node))
#     return -1

# Time: O(E+VlgV), [lgV <- (heappush, heappop)]
# Space: O(V+E)
# Advanced


def dijkstra(path: list, n: int, start: int, destination: int) -> int:
    dist = {}
    weight = defaultdict(dict)
    # create_graph
    for cur, nxt, d in path:
        weight[cur][nxt] = weight[nxt][cur] = d
    pq = [(0, start)]  # [(dist from start to node, node)]
    heapq.heapify(pq)
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_node == destination:
            return cur_dist
        if cur_dist not in dist:  # shortest path always will be reached first
            dist[cur_node] = cur_dist
            for nxt_node, nxt_dist in weight[cur_node].items():
                heapq.heappush(pq, (cur_dist + nxt_dist, nxt_node))
    return -1


print(dijkstra(path, n=4, start=3, destination=0))
