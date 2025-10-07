from collections import defaultdict

class Solution:
    def minRunesToAdd(self, n, flowFrom, flowTo, crystals):
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)
        for u, v in zip(flowFrom, flowTo):
            graph[u].append(v)
            reverse_graph[v].append(u)

        indices = [-1] * n
        low_links = [0] * n
        on_stack = [False] * n
        stack = []
        index = 0
        sccs = []

        def tarjan(node):
            nonlocal index
            indices[node] = index
            low_links[node] = index
            index += 1
            stack.append(node)
            on_stack[node] = True

            for neighbor in graph[node]:
                if indices[neighbor] == -1:
                    tarjan(neighbor)
                    low_links[node] = min(low_links[node], low_links[neighbor])
                elif on_stack[neighbor]:
                    low_links[node] = min(low_links[node], indices[neighbor])

            if low_links[node] == indices[node]:
                scc = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    scc.append(w)
                    if w == node:
                        break
                sccs.append(scc)

        for i in range(n):
            if indices[i] == -1:
                tarjan(i)

        scc_graph = defaultdict(list)
        scc_index = [-1] * n
        scc_has_crystal = [False] * len(sccs)

        crystals_set = set(crystals)
        for i, scc in enumerate(sccs):
            for node in scc:
                scc_index[node] = i
                if node in crystals_set:
                    scc_has_crystal[i] = True

        for u, v in zip(flowFrom, flowTo):
            u_scc = scc_index[u]
            v_scc = scc_index[v]
            if u_scc != v_scc:
                scc_graph[u_scc].append(v_scc)

        in_degree = [0] * len(sccs)
        for scc in range(len(sccs)):
            for neighbor in scc_graph[scc]:
                in_degree[neighbor] += 1

        additional_runes = 0
        for scc in range(len(sccs)):
            if in_degree[scc] == 0 and not scc_has_crystal[scc]:
                additional_runes += 1

        return additional_runes