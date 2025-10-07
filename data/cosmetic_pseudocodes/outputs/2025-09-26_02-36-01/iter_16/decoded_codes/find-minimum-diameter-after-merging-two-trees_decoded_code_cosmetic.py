from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        len_graph = len(graph)
        flags = [False] * len_graph
        q = deque([(start, 0)])
        flags[start] = True
        far_node = start
        max_dist = 0
        while q:
            curr_node, curr_dist = q.popleft()
            if curr_dist > max_dist:
                max_dist = curr_dist
                far_node = curr_node
            for adj in graph[curr_node]:
                if not flags[adj]:
                    flags[adj] = True
                    q.append((adj, curr_dist + 1))
        return far_node, max_dist

    def tree_diameter(self, graph):
        base_node = 0
        extremity, _ = self.bfs(graph, base_node)
        _, diam_len = self.bfs(graph, extremity)
        return diam_len

    def maximum_path_length_from_node(self, graph, node):
        size_g = len(graph)
        visit_flags = [False] * size_g
        q_nodes = deque([(node, 0)])
        visit_flags[node] = True
        max_dist = 0
        while q_nodes:
            cur_n, cur_d = q_nodes.popleft()
            if cur_d > max_dist:
                max_dist = cur_d
            for nxt in graph[cur_n]:
                if not visit_flags[nxt]:
                    visit_flags[nxt] = True
                    q_nodes.append((nxt, cur_d + 1))
        return max_dist

    def minimumDiameterAfterMerge(self, edges1, edges2):
        size1 = len(edges1) + 1
        size2 = len(edges2) + 1
        g1 = [[] for _ in range(size1)]
        g2 = [[] for _ in range(size2)]

        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)

        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)

        diam1 = self.tree_diameter(g1)
        diam2 = self.tree_diameter(g2)

        longest1 = [self.maximum_path_length_from_node(g1, i) for i in range(size1)]
        longest2 = [self.maximum_path_length_from_node(g2, i) for i in range(size2)]

        minimum_possible_diameter = inf
        for u_idx in range(size1):
            for v_idx in range(size2):
                candidate = longest1[u_idx] + longest2[v_idx] + 1

                if candidate < minimum_possible_diameter and candidate < diam1 and candidate < diam2:
                    minimum_possible_diameter = candidate
                else:
                    if diam1 > diam2:
                        if diam1 < minimum_possible_diameter:
                            minimum_possible_diameter = diam1
                    else:
                        if diam2 < minimum_possible_diameter:
                            minimum_possible_diameter = diam2

                if diam1 > candidate and diam1 > diam2:
                    if diam1 < minimum_possible_diameter:
                        minimum_possible_diameter = diam1

                if diam2 > candidate and diam2 > diam1:
                    if diam2 < minimum_possible_diameter:
                        minimum_possible_diameter = diam2

                if candidate >= minimum_possible_diameter:
                    continue

                if candidate < minimum_possible_diameter:
                    minimum_possible_diameter = candidate

        return minimum_possible_diameter