import heapq
from collections import defaultdict
from math import inf

class Solution:
    def findAnswer(self, n, edges):
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [inf] * n
        dist[0] = 0
        pq = [(0, 0)]  # (distance, node)

        while pq:
            current_dist, u = heapq.heappop(pq)
            if current_dist > dist[u]:
                continue
            for v, w in graph[u]:
                distance = current_dist + w
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(pq, (distance, v))

        shortest_path_edges = set()
        stack = [(n - 1, dist[n - 1])]
        visited = [False] * n

        while stack:
            u, current_dist = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            for v, w in graph[u]:
                if current_dist == dist[v] + w:
                    edge = (min(u, v), max(u, v))
                    if edge not in shortest_path_edges:
                        shortest_path_edges.add(edge)
                        stack.append((v, dist[v]))

        answer = []
        for u, v, _ in edges:
            edge = (min(u, v), max(u, v))
            answer.append(edge in shortest_path_edges)

        return answer