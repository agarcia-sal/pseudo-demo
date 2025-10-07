from collections import defaultdict
from typing import List

class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: List[int]) -> int:
        adj = defaultdict(list)
        rev_adj = defaultdict(list)

        for i in range(len(flowFrom)):
            start_node = flowFrom[i]
            end_node = flowTo[i]
            adj[start_node].append(end_node)
            rev_adj[end_node].append(start_node)

        current_index = 0
        stack_nodes = []
        visited_stack = [False] * n
        node_index = [-1] * n
        node_lowlink = [0] * n
        strongly_connected_components = []

        def tarjanDFS(vertex):
            nonlocal current_index
            node_index[vertex] = current_index
            node_lowlink[vertex] = current_index
            current_index += 1
            stack_nodes.append(vertex)
            visited_stack[vertex] = True

            for neighbor in adj.get(vertex, []):
                if node_index[neighbor] == -1:
                    tarjanDFS(neighbor)
                    node_lowlink[vertex] = min(node_lowlink[vertex], node_lowlink[neighbor])
                elif visited_stack[neighbor]:
                    node_lowlink[vertex] = min(node_lowlink[vertex], node_index[neighbor])

            if node_lowlink[vertex] == node_index[vertex]:
                component = []
                while True:
                    w = stack_nodes.pop()
                    visited_stack[w] = False
                    component.append(w)
                    if w == vertex:
                        break
                strongly_connected_components.append(component)

        for node in range(n):
            if node_index[node] == -1:
                tarjanDFS(node)

        scc_map = [-1] * n
        scc_contains_crystal = [False] * len(strongly_connected_components)

        crystal_set = set(crystals)
        for idx_scc, comp in enumerate(strongly_connected_components):
            for member_node in comp:
                scc_map[member_node] = idx_scc
                if member_node in crystal_set:
                    scc_contains_crystal[idx_scc] = True

        condensed_graph = defaultdict(list)
        for i in range(len(flowFrom)):
            src_scc = scc_map[flowFrom[i]]
            dst_scc = scc_map[flowTo[i]]
            if src_scc != dst_scc:
                condensed_graph[src_scc].append(dst_scc)

        in_degree_scc = [0] * len(strongly_connected_components)
        for scc_node in range(len(strongly_connected_components)):
            for neighbor_scc in condensed_graph.get(scc_node, []):
                in_degree_scc[neighbor_scc] += 1

        count_new_runes = 0
        for scc_node in range(len(strongly_connected_components)):
            if in_degree_scc[scc_node] == 0 and not scc_contains_crystal[scc_node]:
                count_new_runes += 1

        return count_new_runes