from collections import defaultdict
from typing import List

class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: List[int]) -> int:
        mappingA = defaultdict(list)  # adjacency list
        mappingB = defaultdict(list)  # reverse adjacency list (not directly used beyond construction but kept for faithfulness)

        idx_counter = 0
        indices_array = [-1] * n
        lows_array = [0] * n
        stack_flags = [False] * n
        node_stack = []
        components_list = []

        def explore(node: int) -> None:
            nonlocal idx_counter
            indices_array[node] = idx_counter
            lows_array[node] = idx_counter
            idx_counter += 1
            node_stack.append(node)
            stack_flags[node] = True

            neighbors_iter = mappingA.get(node, [])
            pos = 0
            while pos < len(neighbors_iter):
                current_neighbor = neighbors_iter[pos]
                if indices_array[current_neighbor] == -1:
                    explore(current_neighbor)
                    lows_array[node] = min(lows_array[node], lows_array[current_neighbor])
                elif stack_flags[current_neighbor]:
                    lows_array[node] = min(lows_array[node], indices_array[current_neighbor])
                pos += 1

            if lows_array[node] == indices_array[node]:
                component_nodes = []
                while True:
                    popped_node = node_stack.pop()
                    stack_flags[popped_node] = False
                    component_nodes.append(popped_node)
                    if popped_node == node:
                        break
                components_list.append(component_nodes)

        # Build adjacency lists
        pos_flowFrom = 0
        while pos_flowFrom < len(flowFrom):
            elem_u = flowFrom[pos_flowFrom]
            elem_v = flowTo[pos_flowFrom]
            mappingA[elem_u].append(elem_v)
            mappingB[elem_v].append(elem_u)
            pos_flowFrom += 1

        # Run Tarjan's algorithm to find strongly connected components (SCCs)
        idx = 0
        while idx < n:
            if indices_array[idx] == -1:
                explore(idx)
            idx += 1

        scc_mappings = defaultdict(list)
        node_to_scc = [-1] * n
        scc_presence_flags = [False] * len(components_list)
        count_scc = 0

        for idx_component, current_scc in enumerate(components_list):
            for node_item in current_scc:
                node_to_scc[node_item] = count_scc
                if node_item in crystals:
                    scc_presence_flags[idx_component] = True
            count_scc += 1

        pos_edge = 0
        while pos_edge < len(flowFrom):
            start_node = flowFrom[pos_edge]
            end_node = flowTo[pos_edge]
            start_scc = node_to_scc[start_node]
            end_scc = node_to_scc[end_node]
            if start_scc != end_scc:
                scc_mappings[start_scc].append(end_scc)
            pos_edge += 1

        in_degrees = [0] * len(components_list)
        scc_index_iter = 0
        while scc_index_iter < len(components_list):
            neighbors_list = scc_mappings.get(scc_index_iter, [])
            neighbor_ptr = 0
            while neighbor_ptr < len(neighbors_list):
                neighbor_node = neighbors_list[neighbor_ptr]
                in_degrees[neighbor_node] += 1
                neighbor_ptr += 1
            scc_index_iter += 1

        needed_runes = 0
        scc_check = 0
        while scc_check < len(components_list):
            if in_degrees[scc_check] == 0 and not scc_presence_flags[scc_check]:
                needed_runes += 1
            scc_check += 1

        return needed_runes