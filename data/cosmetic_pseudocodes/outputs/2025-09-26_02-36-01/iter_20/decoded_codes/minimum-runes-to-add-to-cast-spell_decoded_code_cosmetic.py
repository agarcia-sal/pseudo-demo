class Solution:
    def minRunesToAdd(self, n, flowFrom, flowTo, crystals):
        def buildAdjacency(srcList, destList, graph_map):
            for idx in range(len(srcList)):
                keyX = srcList[idx]
                valY = destList[idx]
                if keyX not in graph_map:
                    graph_map[keyX] = []
                if valY not in graph_map:
                    graph_map[valY] = []
                graph_map[keyX].append(valY)

        graph = {}
        reverse_graph = {}
        buildAdjacency(flowFrom, flowTo, graph)
        buildAdjacency(flowTo, flowFrom, reverse_graph)

        indices = [-1] * n
        low_links = [0] * n
        on_stack = [False] * n
        stack = []
        current_index = 0
        sccs = []

        def tarjan(node):
            nonlocal current_index
            indices[node] = current_index
            low_links[node] = current_index
            current_index += 1
            stack.append(node)
            on_stack[node] = True

            for neighbor in graph.get(node, []):
                if indices[neighbor] == -1:
                    tarjan(neighbor)
                    if low_links[node] > low_links[neighbor]:
                        low_links[node] = low_links[neighbor]
                elif on_stack[neighbor]:
                    if low_links[node] > indices[neighbor]:
                        low_links[node] = indices[neighbor]

            if low_links[node] == indices[node]:
                component = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    component.append(w)
                    if w == node:
                        break
                sccs.append(component)

        for i in range(n):
            if indices[i] == -1:
                tarjan(i)

        scc_graph = {}
        scc_index = [-1] * n
        scc_has_crystal = [False] * len(sccs)

        for idx, component in enumerate(sccs):
            for node in component:
                scc_index[node] = idx
                if node in crystals:
                    scc_has_crystal[idx] = True

        for j in range(len(flowFrom)):
            u_k = flowFrom[j]
            v_k = flowTo[j]
            u_scc = scc_index[u_k]
            v_scc = scc_index[v_k]
            if u_scc != v_scc:
                if u_scc not in scc_graph:
                    scc_graph[u_scc] = []
                scc_graph[u_scc].append(v_scc)

        in_degree = [0] * len(sccs)
        for scc_iter in range(len(sccs)):
            if scc_iter in scc_graph:
                for nbr in scc_graph[scc_iter]:
                    in_degree[nbr] += 1

        additions = 0
        for idxC in range(len(sccs)):
            if in_degree[idxC] == 0 and not scc_has_crystal[idxC]:
                additions += 1

        return additions