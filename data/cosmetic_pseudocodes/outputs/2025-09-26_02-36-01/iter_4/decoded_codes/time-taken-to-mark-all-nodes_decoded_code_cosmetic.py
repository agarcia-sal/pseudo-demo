from collections import deque

class Solution:
    def timeTaken(self, edges):
        totalNodes = len(edges) + 1

        def construct_adjacency_list(edges):
            adjacency_map = [[] for _ in range(totalNodes)]
            for u, v in edges:
                adjacency_map[u].append(v)
                adjacency_map[v].append(u)
            return adjacency_map

        adjacency_map = construct_adjacency_list(edges)

        def bfs(origin):
            deq = deque([(origin, 0)])
            seen = [False] * totalNodes
            seen[origin] = True
            highest_time = 0

            while deq:
                node, elapsed = deq.popleft()
                if elapsed > highest_time:
                    highest_time = elapsed

                for adj_node in adjacency_map[node]:
                    if not seen[adj_node]:
                        seen[adj_node] = True
                        remainder_val = adj_node % 2
                        if remainder_val == 0:
                            deq.append((adj_node, elapsed + 2))
                        else:
                            deq.append((adj_node, elapsed + 1))
            return highest_time

        result_times = [0] * totalNodes
        idx = 0
        while idx <= totalNodes - 1:
            result_times[idx] = bfs(idx)
            idx += 1

        return result_times