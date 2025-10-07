import heapq
from collections import defaultdict
from math import inf

class Solution:
    def findAnswer(self, n, edges):
        adjacency_dict = defaultdict(list)
        for edge in edges:
            u, v, w = edge
            adjacency_dict[u].append((v, w))
            adjacency_dict[v].append((u, w))

        distance_list = [inf] * n
        distance_list[0] = 0
        min_heap = [(0, 0)]

        while min_heap:
            curr_distance, node = heapq.heappop(min_heap)
            if curr_distance > distance_list[node]:
                continue
            for neighbor, weight in adjacency_dict[node]:
                tentative_distance = curr_distance + weight
                if tentative_distance < distance_list[neighbor]:
                    distance_list[neighbor] = tentative_distance
                    heapq.heappush(min_heap, (tentative_distance, neighbor))

        edge_set = set()
        dfs_stack = [(n - 1, distance_list[n - 1])]
        seen_list = [False] * n

        while dfs_stack:
            current_node, dist_val = dfs_stack.pop()
            if seen_list[current_node]:
                continue
            seen_list[current_node] = True
            for adj_node, adj_weight in adjacency_dict[current_node]:
                if dist_val == distance_list[adj_node] + adj_weight:
                    edge_tuple = (min(current_node, adj_node), max(current_node, adj_node))
                    if edge_tuple not in edge_set:
                        edge_set.add(edge_tuple)
                        dfs_stack.append((adj_node, distance_list[adj_node]))

        result_list = []
        for edge in edges:
            a, b = edge[0], edge[1]
            normalized_edge = (min(a, b), max(a, b))
            result_list.append(normalized_edge in edge_set)

        return result_list