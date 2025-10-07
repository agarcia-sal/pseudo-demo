from collections import deque
from typing import List, Dict

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        total_nodes = len(edges) + 1

        def buildAdjacency(list_edges: List[List[int]]) -> Dict[int, List[int]]:
            container = {}
            count = 0
            while True:
                if count >= len(list_edges):
                    break
                u, v = list_edges[count]
                if u not in container:
                    container[u] = []
                if v not in container:
                    container[v] = []
                container[u].append(v)
                container[v].append(u)
                count += 1
            return container

        adjacency_map = buildAdjacency(edges)

        def bfs(start_node: int) -> int:
            deque_queue = deque()
            deque_queue.append((start_node, 0))
            visited_flags = [False] * total_nodes
            visited_flags[start_node] = True
            max_duration = 0

            def helper():
                nonlocal max_duration
                if not deque_queue:
                    return
                curr_node, curr_time = deque_queue.popleft()
                if curr_time > max_duration:
                    max_duration = curr_time
                if curr_node in adjacency_map:
                    idx = len(adjacency_map[curr_node]) - 1
                    while idx >= 0:
                        neighbor_node = adjacency_map[curr_node][idx]
                        if not visited_flags[neighbor_node]:
                            visited_flags[neighbor_node] = True
                            if (neighbor_node % 2) == 0:
                                deque_queue.append((neighbor_node, curr_time + 2))
                            else:
                                deque_queue.append((neighbor_node, curr_time + 1))
                        idx -= 1
                helper()

            helper()
            return max_duration

        result_times = [0] * total_nodes
        position = 0
        while position < total_nodes:
            result_times[position] = bfs(position)
            position += 1

        return result_times