from collections import defaultdict
from typing import List

class Solution:
    def minRunesToAdd(self, n: int, flowFrom: List[int], flowTo: List[int], crystals: List[int]) -> int:
        mapAdjacency = defaultdict(list)
        mapReverse = defaultdict(list)

        iter_src = iter(flowFrom)
        iter_dst = iter(flowTo)
        while True:
            try:
                hasSrc = next(iter_src)
                hasDst = next(iter_dst)
            except StopIteration:
                break
            mapAdjacency[hasSrc].append(hasDst)
            mapReverse[hasDst].append(hasSrc)

        idx_vals = [-1] * n
        low_link_vals = [0] * n
        flags_on_stack = [False] * n
        stk = []
        running_index = 0
        scc_collections = []

        def dfs_tarjan(vertex):
            nonlocal running_index
            idx_vals[vertex] = running_index
            low_link_vals[vertex] = running_index
            running_index += 1
            stk.append(vertex)
            flags_on_stack[vertex] = True

            neighbors = mapAdjacency.get(vertex, [])
            for adj_node in neighbors:
                if idx_vals[adj_node] == -1:
                    dfs_tarjan(adj_node)
                    if low_link_vals[adj_node] < low_link_vals[vertex]:
                        low_link_vals[vertex] = low_link_vals[adj_node]
                else:
                    if flags_on_stack[adj_node]:
                        if idx_vals[adj_node] < low_link_vals[vertex]:
                            low_link_vals[vertex] = idx_vals[adj_node]

            if low_link_vals[vertex] == idx_vals[vertex]:
                current_scc = []
                while True:
                    popped_node = stk.pop()
                    flags_on_stack[popped_node] = False
                    current_scc.append(popped_node)
                    if popped_node == vertex:
                        break
                scc_collections.append(current_scc)

        counter = 0
        while counter < n:
            if idx_vals[counter] == -1:
                dfs_tarjan(counter)
            counter += 1

        scc_representation = defaultdict(list)
        map_node_to_scc = [-1] * n
        has_crystal_flag = [False] * len(scc_collections)
        scc_id = 0

        for idx_scc, arr_nodes in enumerate(scc_collections):
            for nodeElem in arr_nodes:
                map_node_to_scc[nodeElem] = scc_id
                if nodeElem in crystals:
                    has_crystal_flag[idx_scc] = True
            scc_id += 1

        iter_u = iter(flowFrom)
        iter_v = iter(flowTo)
        while True:
            try:
                val_u = next(iter_u)
                val_v = next(iter_v)
            except StopIteration:
                break
            scc_u = map_node_to_scc[val_u]
            scc_v = map_node_to_scc[val_v]
            if scc_u != scc_v:
                scc_representation[scc_u].append(scc_v)

        in_deg_list = [0] * len(scc_collections)
        idx_scc2 = 0
        while idx_scc2 < len(scc_collections):
            if idx_scc2 in scc_representation:
                for neighbor_scc in scc_representation[idx_scc2]:
                    in_deg_list[neighbor_scc] += 1
            idx_scc2 += 1

        needed_runes = 0
        idx_scc3 = 0
        while idx_scc3 < len(scc_collections):
            if in_deg_list[idx_scc3] == 0 and not has_crystal_flag[idx_scc3]:
                needed_runes += 1
            idx_scc3 += 1

        return needed_runes