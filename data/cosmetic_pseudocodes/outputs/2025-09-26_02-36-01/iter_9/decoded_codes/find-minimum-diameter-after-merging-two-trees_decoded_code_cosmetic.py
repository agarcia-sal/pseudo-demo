from math import inf

class Solution:
    def bfs(self, graph, start):
        def DequePopLeft(q):
            return q.pop(0)

        def DequeAppend(q, x):
            q.append(x)

        count_nodes = len(graph)
        marks = [False] * count_nodes

        queue_container = []
        DequeAppend(queue_container, (start, 0))
        marks[start] = True

        last_node = start
        max_dist = 0

        while queue_container:
            cur_node, cur_dist = DequePopLeft(queue_container)

            if cur_dist > max_dist:
                max_dist = cur_dist
                last_node = cur_node

            for adj_node in graph[cur_node]:
                if not marks[adj_node]:
                    marks[adj_node] = True
                    DequeAppend(queue_container, (adj_node, cur_dist + 1))

        return last_node, max_dist

    def tree_diameter(self, graph):
        st_node = 0
        _, farthest = self.bfs(graph, st_node)
        _, diam_value = self.bfs(graph, farthest)
        return diam_value

    def maximum_path_length_from_node(self, graph, node):
        def DequePopLeft(q):
            return q.pop(0)

        def DequeAppend(q, y):
            q.append(y)

        total_nodes = len(graph)
        flag_marks = [False] * total_nodes

        queue_list = []
        DequeAppend(queue_list, (node, 0))
        flag_marks[node] = True

        max_len = 0

        while queue_list:
            cur_n, cur_d = DequePopLeft(queue_list)

            if cur_d > max_len:
                max_len = cur_d

            for adj in graph[cur_n]:
                if not flag_marks[adj]:
                    flag_marks[adj] = True
                    DequeAppend(queue_list, (adj, cur_d + 1))

        return max_len

    def minimumDiameterAfterMerge(self, edges1, edges2):
        def AppendEdge(g_list, u_val, v_val):
            g_list[u_val].append(v_val)
            g_list[v_val].append(u_val)

        length1 = len(edges1) + 1
        length2 = len(edges2) + 1

        graphA = [[] for _ in range(length1)]
        graphB = [[] for _ in range(length2)]

        for u, v in edges1:
            AppendEdge(graphA, u, v)

        for u, v in edges2:
            AppendEdge(graphB, u, v)

        dia1 = self.tree_diameter(graphA)
        dia2 = self.tree_diameter(graphB)

        longest_paths_A = [self.maximum_path_length_from_node(graphA, idxA) for idxA in range(length1)]
        longest_paths_B = [self.maximum_path_length_from_node(graphB, idxB) for idxB in range(length2)]

        min_diam_candidate = inf

        for valA in longest_paths_A:
            for valB in longest_paths_B:
                comp1 = dia1
                comp2 = dia2
                comp3 = valA + valB + 1

                if comp1 >= comp2:
                    if comp1 >= comp3:
                        max_val = comp1
                    else:
                        max_val = comp3
                else:
                    if comp2 >= comp3:
                        max_val = comp2
                    else:
                        max_val = comp3

                if max_val < min_diam_candidate:
                    min_diam_candidate = max_val

        return min_diam_candidate