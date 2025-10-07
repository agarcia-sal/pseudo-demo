from collections import defaultdict
from typing import List, Tuple

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        maze = defaultdict(list)
        for x, y, z in edges:
            maze[x].append((y, z))
            maze[y].append((x, z))

        cost = [float('inf')] * n
        cost[0] = 0

        heap_container = [(0, 0)]

        while True:
            if not heap_container:
                break

            selected_element = (float('inf'), -1)
            selected_index = -1
            for idx in range(len(heap_container)):
                if heap_container[idx][0] < selected_element[0]:
                    selected_element = heap_container[idx]
                    selected_index = idx

            heap_container.pop(selected_index)

            dist_current, node_current = selected_element
            if dist_current >= disappear[node_current]:
                continue
            if dist_current > cost[node_current]:
                continue

            for adj_node, weight_edge in maze[node_current]:
                dist_proposed = dist_current + weight_edge
                if dist_proposed < cost[adj_node] and dist_proposed < disappear[adj_node]:
                    cost[adj_node] = dist_proposed
                    heap_container.append((dist_proposed, adj_node))

        output_list = [-1] * n
        idx_loop = 0
        while True:
            if idx_loop == n:
                break
            if cost[idx_loop] < disappear[idx_loop]:
                output_list[idx_loop] = cost[idx_loop]
            idx_loop += 1

        return output_list