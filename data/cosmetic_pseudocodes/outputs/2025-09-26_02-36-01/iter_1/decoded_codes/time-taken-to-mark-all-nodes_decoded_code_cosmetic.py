from collections import deque
from typing import List, Dict

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        node_count = len(edges) + 1
        adjacency_map: Dict[int, List[int]] = {}

        for u, v in edges:
            if u not in adjacency_map:
                adjacency_map[u] = []
            if v not in adjacency_map:
                adjacency_map[v] = []
            adjacency_map[u].append(v)
            adjacency_map[v].append(u)

        def bfs(source: int) -> int:
            visited_nodes = [False] * node_count
            bfs_queue = deque()
            bfs_queue.append((source, 0))
            visited_nodes[source] = True
            longest_duration = 0

            while bfs_queue:
                current_node, elapsed_time = bfs_queue.popleft()
                if elapsed_time > longest_duration:
                    longest_duration = elapsed_time

                for adjacent_node in adjacency_map.get(current_node, []):
                    if not visited_nodes[adjacent_node]:
                        visited_nodes[adjacent_node] = True
                        add_time = 2 if adjacent_node % 2 == 0 else 1
                        bfs_queue.append((adjacent_node, elapsed_time + add_time))

            return longest_duration

        result_times = [0] * node_count
        for index in range(node_count):
            result_times[index] = bfs(index)

        return result_times