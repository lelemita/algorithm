# 그래프 > 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
# Depth-First Search (DFS) - Stack, Recursive
# Breadth-First Search (BFS) - Queue
# 1차: 7, 8, 9번 케이스 시간 초과
from collections import Counter
from queue import Queue


def solution(n, edges):
    nodes = Queue()
    nodes.put(1)
    dist = {1: 0}
    while not nodes.empty():
        here = nodes.get()
        for idx, edge in enumerate(edges):
            adj = edge[0] if here == edge[1] else edge[1] if here == edge[0] else -1
            if adj > 0 and adj not in dist.keys():
                nodes.put(adj)
                dist[adj] = min(dist.get(adj, dist[here] + 1), dist[here] + 1)
    cnts = Counter(dist.values())
    maxi = max(cnts.keys())
    return cnts[maxi]


if __name__ == "__main__":
    print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
    print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
    print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 3)
    print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
    print(solution(2, [[1, 2]]), 1)
    print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
    print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
    print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)
