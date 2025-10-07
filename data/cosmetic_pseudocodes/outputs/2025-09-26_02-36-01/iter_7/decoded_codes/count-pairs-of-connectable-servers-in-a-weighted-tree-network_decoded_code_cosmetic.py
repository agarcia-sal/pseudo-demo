from collections import defaultdict
from typing import List

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        adjacency_map = defaultdict(list)

        def buildGraph(index: int) -> None:
            if index == len(edges):
                return
            src, tgt, wgt = edges[index]
            adjacency_map[src].append([tgt, wgt])
            adjacency_map[tgt].append([src, wgt])
            buildGraph(index + 1)

        buildGraph(0)

        total_nodes = len(adjacency_map)
        results_array = [0] * total_nodes

        def depthSearch(curr_node: int, prev_node: int, dist: int, collected_nodes: List[int]) -> int:
            mod_result = dist % signalSpeed
            if mod_result == 0:
                collected_nodes.append(curr_node)
            acc_count = 0
            neighbors_list = adjacency_map[curr_node]
            for adj_node, edge_wgt in neighbors_list:
                if adj_node != prev_node:
                    acc_count += depthSearch(adj_node, curr_node, dist + edge_wgt, collected_nodes)
            if mod_result == 0:
                return acc_count + 1
            else:
                return acc_count

        def pairsCountViaCenter(center_node: int) -> int:
            collected_paths = []
            neighbors_for_center = adjacency_map[center_node]
            for neighbor_node, neighbor_wgt in neighbors_for_center:
                current_path = []
                depthSearch(neighbor_node, center_node, neighbor_wgt, current_path)
                collected_paths.append(current_path)

            combined_pairs = 0
            for m in range(len(collected_paths) - 1):
                len_m = len(collected_paths[m])
                for n in range(m + 1, len(collected_paths)):
                    len_n = len(collected_paths[n])
                    combined_pairs += len_m * len_n
            return combined_pairs

        for iterator in range(total_nodes):
            results_array[iterator] = pairsCountViaCenter(iterator)

        return results_array