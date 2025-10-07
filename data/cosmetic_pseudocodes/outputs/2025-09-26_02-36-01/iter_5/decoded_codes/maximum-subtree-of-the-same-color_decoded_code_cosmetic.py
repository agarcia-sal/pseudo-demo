from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        adjacency = defaultdict(list)

        def add_edge(a: int, b: int) -> None:
            adjacency[a].append(b)
            adjacency[b].append(a)

        for origin, target in edges:
            add_edge(origin, target)

        maximum_result = 1

        def dfs(current_node: int, ancestor_node: int) -> int:
            nonlocal maximum_result
            uniform_color_nodes = 1
            children_uniform_color_flag = True
            neighbor_index = 0

            def iterate_neighbors():
                nonlocal neighbor_index, uniform_color_nodes, children_uniform_color_flag
                if neighbor_index >= len(adjacency[current_node]):
                    return
                adjacent_node = adjacency[current_node][neighbor_index]
                neighbor_index += 1
                if adjacent_node != ancestor_node:
                    subtree_size = dfs(adjacent_node, current_node)
                    if subtree_size == 0:
                        children_uniform_color_flag = False
                    else:
                        if colors[adjacent_node] == colors[current_node]:
                            uniform_color_nodes_local = uniform_color_nodes + subtree_size
                            uniform_color_nodes = uniform_color_nodes_local
                        else:
                            children_uniform_color_flag = False
                iterate_neighbors()

            iterate_neighbors()

            if children_uniform_color_flag:
                if uniform_color_nodes > maximum_result:
                    maximum_result = uniform_color_nodes
                return uniform_color_nodes
            else:
                return 0

        start_node = 0
        root_parent = -1
        dfs(start_node, root_parent)
        return maximum_result