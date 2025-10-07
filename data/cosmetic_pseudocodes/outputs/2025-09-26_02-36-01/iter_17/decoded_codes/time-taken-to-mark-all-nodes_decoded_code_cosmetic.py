from collections import deque
from typing import List, Tuple, Dict

class Solution:
    def timeTaken(self, edges: List[Tuple[int, int]]) -> List[int]:
        m = len(edges) + 1

        def construct_adjacency_list(edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
            graph = {i: [] for i in range(m)}
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        graph_map = construct_adjacency_list(edges)

        def bfs(root: int) -> int:
            line_queue = deque([(root, 0)])
            marked = [False] * m
            marked[root] = True
            peak_time = 0

            while line_queue:
                current_node, node_time = line_queue.popleft()
                if peak_time < node_time:
                    peak_time = node_time

                for adj_node in graph_map[current_node]:
                    if not marked[adj_node]:
                        marked[adj_node] = True
                        if adj_node % 2 == 0:
                            new_time = node_time + 2
                        else:
                            new_time = node_time + 1
                        line_queue.append((adj_node, new_time))

            return peak_time

        result_times = [0] * m
        for idx in range(m):
            result_times[idx] = bfs(idx)

        return result_times