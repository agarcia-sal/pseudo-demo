from collections import defaultdict, deque
from typing import List, Tuple


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        connection_map_1 = defaultdict(list)
        connection_map_2 = defaultdict(list)

        def build_connections(edge_list: List[List[int]], connection_map: defaultdict) -> None:
            idx = 0
            while idx < len(edge_list):
                src_dest = edge_list[idx]
                node_x, node_y = src_dest[0], src_dest[1]
                connection_map[node_x].append(node_y)
                connection_map[node_y].append(node_x)
                idx += 1

        build_connections(edges1, connection_map_1)
        build_connections(edges2, connection_map_2)

        # Determine max node index in each connection map to define size
        # Since keys could be sparse, find the maximum index key to ensure coverage
        size_1 = max(connection_map_1.keys()) + 1 if connection_map_1 else 0
        size_2 = max(connection_map_2.keys()) + 1 if connection_map_2 else 0

        def bfs(tree_structure: defaultdict, origin_node: int) -> Tuple[int, int]:
            count_even_dist = 0
            count_odd_dist = 0
            deque_nodes = deque([(origin_node, 0)])
            visited_nodes = {origin_node}

            while deque_nodes:
                current_node, current_distance = deque_nodes.popleft()
                if current_distance % 2 == 0:
                    count_even_dist += 1
                else:
                    count_odd_dist += 1

                for adj_node in tree_structure.get(current_node, []):
                    if adj_node not in visited_nodes:
                        visited_nodes.add(adj_node)
                        deque_nodes.append((adj_node, current_distance + 1))

            return count_even_dist, count_odd_dist

        list_even_odd_1 = []
        index_1 = 0
        while index_1 < size_1:
            list_even_odd_1.append(bfs(connection_map_1, index_1))
            index_1 += 1

        list_even_odd_2 = []
        index_2 = 0
        while index_2 < size_2:
            list_even_odd_2.append(bfs(connection_map_2, index_2))
            index_2 += 1

        output_accum = []

        for outer_idx in range(size_1):
            even_1, odd_1 = list_even_odd_1[outer_idx]
            max_found_targets = 0

            inner_idx = 0
            while inner_idx < size_2:
                even_2, odd_2 = list_even_odd_2[inner_idx]

                condition1 = (outer_idx == inner_idx)
                condition2 = ((outer_idx % 2) == (inner_idx % 2))

                if condition1 or condition2:
                    candidate_targets = even_2
                else:
                    candidate_targets = odd_2

                if candidate_targets > max_found_targets:
                    max_found_targets = candidate_targets

                inner_idx += 1

            output_accum.append(even_1 + max_found_targets)

        return output_accum