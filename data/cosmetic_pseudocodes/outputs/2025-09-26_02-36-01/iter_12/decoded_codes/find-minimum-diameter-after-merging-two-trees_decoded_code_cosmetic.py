from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        def pop_left(queue):
            return queue.popleft()

        def is_empty(container):
            return len(container) == 0

        totalNodes = len(graph)

        visited_flags = [False] * totalNodes

        q_container = deque()
        q_container.append((start, 0))

        visited_flags[start] = True

        currentFarthest = start
        currentMaxDist = 0

        while not is_empty(q_container):
            currentNode, currentDist = pop_left(q_container)

            if currentDist > currentMaxDist:
                currentMaxDist = currentDist
                currentFarthest = currentNode

            neighbors_iter = graph[currentNode]
            idx2 = 0
            while idx2 < len(neighbors_iter):
                neighbor_candidate = neighbors_iter[idx2]
                if not visited_flags[neighbor_candidate]:
                    visited_flags[neighbor_candidate] = True
                    q_container.append((neighbor_candidate, currentDist + 1))
                idx2 += 1

        return currentFarthest, currentMaxDist

    def tree_diameter(self, graph):
        initNode = 0

        def call_bfs1():
            return self.bfs(graph, initNode)

        far_node, _unused1 = call_bfs1()

        def call_bfs2():
            return self.bfs(graph, far_node)

        _unused2, diam_value = call_bfs2()

        return diam_value

    def maximum_path_length_from_node(self, graph, node):
        def pop_left(queue):
            return queue.popleft()

        def is_empty(container):
            return len(container) == 0

        totalAmount = len(graph)

        visitFlags = [False] * totalAmount

        q_list = deque()
        q_list.append((node, 0))

        visitFlags[node] = True

        maxDistanceVal = 0

        while not is_empty(q_list):
            currNode, currDist = pop_left(q_list)

            if currDist > maxDistanceVal:
                maxDistanceVal = currDist

            adj_nodes = graph[currNode]
            idx4 = 0
            while idx4 < len(adj_nodes):
                currNeighbor = adj_nodes[idx4]
                if not visitFlags[currNeighbor]:
                    visitFlags[currNeighbor] = True
                    q_list.append((currNeighbor, currDist + 1))
                idx4 += 1

        return maxDistanceVal

    def minimumDiameterAfterMerge(self, edges1, edges2):
        def append_edge(graph, u, v):
            graph[u].append(v)
            graph[v].append(u)

        len1 = len(edges1)
        len2 = len(edges2)

        n_nodes = len1 + 1
        m_nodes = len2 + 1

        graph_1 = [[] for _ in range(n_nodes)]
        graph_2 = [[] for _ in range(m_nodes)]

        edgeIdx1 = 0
        while edgeIdx1 < len1:
            u_val, v_val = edges1[edgeIdx1]
            append_edge(graph_1, u_val, v_val)
            edgeIdx1 += 1

        edgeIdx2 = 0
        while edgeIdx2 < len2:
            u_val2, v_val2 = edges2[edgeIdx2]
            append_edge(graph_2, u_val2, v_val2)
            edgeIdx2 += 1

        diam_1 = self.tree_diameter(graph_1)
        diam_2 = self.tree_diameter(graph_2)

        longest_paths_1 = []
        i1 = 0
        while i1 < n_nodes:
            path_len = self.maximum_path_length_from_node(graph_1, i1)
            longest_paths_1.append(path_len)
            i1 += 1

        longest_paths_2 = []
        i2 = 0
        while i2 < m_nodes:
            path_len2 = self.maximum_path_length_from_node(graph_2, i2)
            longest_paths_2.append(path_len2)
            i2 += 1

        min_diam = inf

        u_idx = 0
        while u_idx < n_nodes:
            v_idx = 0
            while v_idx < m_nodes:
                candidate_diam1 = diam_1
                if diam_2 > candidate_diam1:
                    candidate_diam1 = diam_2

                temp_sum = longest_paths_1[u_idx] + longest_paths_2[v_idx] + 1
                if temp_sum > candidate_diam1:
                    candidate_diam1 = temp_sum

                if candidate_diam1 < min_diam:
                    min_diam = candidate_diam1
                v_idx += 1
            u_idx += 1

        return min_diam