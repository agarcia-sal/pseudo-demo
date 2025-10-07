from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edges: List[Tuple[int, int, int]], signalSpeed: int) -> List[int]:
        adjacency = defaultdict(list)
        for origin, destination, weight in edges:
            adjacency[origin].append((destination, weight))
            adjacency[destination].append((origin, weight))

        node_count = len(adjacency)
        final_counts = [0] * node_count

        def dfs(node: int, parent: int, curr_dist: int, acc_path: List[int]) -> int:
            dist_mod = curr_dist % signalSpeed
            if dist_mod == 0:
                acc_path.append(node)

            subtree_count = 0
            for adj_node, edge_weight in adjacency[node]:
                if adj_node != parent:
                    subtree_count += dfs(adj_node, node, curr_dist + edge_weight, acc_path)

            return subtree_count + 1 if dist_mod == 0 else subtree_count

        def count_pairs_through_c(c: int) -> int:
            collected_paths = []
            for nbr, wgt in adjacency[c]:
                current_path = []
                dfs(nbr, c, wgt, current_path)
                collected_paths.append(current_path)

            pair_total = 0
            length = len(collected_paths)
            for outer in range(length - 1):
                left_size = len(collected_paths[outer])
                for inner in range(outer + 1, length):
                    right_size = len(collected_paths[inner])
                    pair_total += left_size * right_size
            return pair_total

        for counter in range(node_count):
            final_counts[counter] = count_pairs_through_c(counter)

        return final_counts