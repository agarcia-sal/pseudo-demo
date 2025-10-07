from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        n = len(graph)
        visited = [False] * n
        queue = deque([(start, 0)])
        visited[start] = True
        farthest_node = start
        max_distance = 0

        while queue:
            node, dist = queue.popleft()
            if dist > max_distance:
                max_distance = dist
                farthest_node = node
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
        return farthest_node, max_distance

    def tree_diameter(self, graph):
        start = 0
        far_node, _ = self.bfs(graph, start)
        _, diameter = self.bfs(graph, far_node)
        return diameter

    def maximum_path_length_from_node(self, graph, node):
        n = len(graph)
        visited = [False] * n
        queue = deque([(node, 0)])
        visited[node] = True
        max_dist = 0

        while queue:
            current_node, dist = queue.popleft()
            if dist > max_dist:
                max_dist = dist
            for neighbor in graph[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))
        return max_dist

    def minimumDiameterAfterMerge(self, edges1, edges2):
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1

        graph1 = [[] for _ in range(n1)]
        graph2 = [[] for _ in range(n2)]

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        diameter1 = self.tree_diameter(graph1)
        diameter2 = self.tree_diameter(graph2)

        max_paths1 = [self.maximum_path_length_from_node(graph1, i) for i in range(n1)]
        max_paths2 = [self.maximum_path_length_from_node(graph2, i) for i in range(n2)]

        min_diameter = inf

        for i in range(n1):
            for j in range(n2):
                combined = max(diameter1, diameter2, max_paths1[i] + 1 + max_paths2[j])
                if combined < min_diameter:
                    min_diameter = combined

        return min_diameter