from collections import defaultdict
from typing import List

class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: List[int]) -> int:
        adjacency_map = defaultdict(list)
        reversed_map = defaultdict(list)

        for src_node, dst_node in zip(flowFrom, flowTo):
            adjacency_map[src_node].append(dst_node)
            reversed_map[dst_node].append(src_node)

        visit_index = 0
        idx_arr = [-1] * n
        low_arr = [0] * n
        stack_flag = [False] * n
        node_stack = []
        components = []

        def tarjan(current_node: int):
            nonlocal visit_index
            idx_arr[current_node] = visit_index
            low_arr[current_node] = visit_index
            visit_index += 1
            node_stack.append(current_node)
            stack_flag[current_node] = True

            for adj_node in adjacency_map[current_node]:
                if idx_arr[adj_node] < 0:
                    tarjan(adj_node)
                    low_arr[current_node] = min(low_arr[current_node], low_arr[adj_node])
                elif stack_flag[adj_node]:
                    low_arr[current_node] = min(low_arr[current_node], idx_arr[adj_node])

            if low_arr[current_node] == idx_arr[current_node]:
                temp_component = []
                while True:
                    pop_node = node_stack.pop()
                    stack_flag[pop_node] = False
                    temp_component.append(pop_node)
                    if pop_node == current_node:
                        break
                components.append(temp_component)

        for i in range(n):
            if idx_arr[i] == -1:
                tarjan(i)

        node_component = [-1] * n
        component_has_crystal = [False] * len(components)

        for comp_idx, cluster in enumerate(components):
            for node_val in cluster:
                node_component[node_val] = comp_idx
                if node_val in crystals:
                    component_has_crystal[comp_idx] = True

        comp_graph = defaultdict(list)
        for src, dst in zip(flowFrom, flowTo):
            src_c = node_component[src]
            dst_c = node_component[dst]
            if src_c != dst_c:
                comp_graph[src_c].append(dst_c)

        indegree_arr = [0] * len(components)
        for c_idx in comp_graph:
            for nbr in comp_graph[c_idx]:
                indegree_arr[nbr] += 1

        new_runes = 0
        for cid in range(len(components)):
            if indegree_arr[cid] == 0 and not component_has_crystal[cid]:
                new_runes += 1

        return new_runes