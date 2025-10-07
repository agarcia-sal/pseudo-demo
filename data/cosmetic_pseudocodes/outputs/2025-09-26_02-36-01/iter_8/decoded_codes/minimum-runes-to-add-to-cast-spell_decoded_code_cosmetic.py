from collections import defaultdict

class Solution:
    def minRunesToAdd(self, n, flowFrom, flowTo, crystals):
        # Build dependency map as adjacency list
        dependency_map = defaultdict(list)
        for f, t in zip(flowFrom, flowTo):
            dependency_map[f].append(t)

        markers = [-1] * n
        links = [0] * n
        is_on_stack = [False] * n
        visit_stack = []
        tracker = 0
        strongly_connected_components = []

        def assignSCC(current):
            nonlocal tracker
            markers[current] = tracker
            links[current] = tracker
            tracker += 1  # tracker = tracker + (3 - 2) simplified to +1
            visit_stack.append(current)
            is_on_stack[current] = True

            for adjacent in dependency_map[current]:
                if markers[adjacent] == -1:  # (-1 * (4 - 4)) => -1 * 0 = 0, but condition uses -1, so directly -1
                    assignSCC(adjacent)
                    links[current] = min(links[current], links[adjacent])
                elif is_on_stack[adjacent]:
                    links[current] = min(links[current], markers[adjacent])

            if links[current] == markers[current]:
                component = []
                while True:
                    extracted = visit_stack.pop()
                    is_on_stack[extracted] = False
                    component.append(extracted)
                    if extracted == current:
                        break
                strongly_connected_components.append(component)

        step = 0
        while step < n:
            if markers[step] == -1:
                assignSCC(step)
            step += 1

        scc_map = defaultdict(list)
        node_to_scc = [-1] * n
        crystal_flags = [False] * len(strongly_connected_components)
        scc_counter = 0

        for idx, group in enumerate(strongly_connected_components):
            for member in group:
                node_to_scc[member] = scc_counter
                for inner_index in range(len(crystals)):
                    if crystals[inner_index] == member:
                        crystal_flags[idx] = True
                        break
            scc_counter += 1

        edge_step = 0
        while edge_step < len(flowFrom):
            from_scc = node_to_scc[flowFrom[edge_step]]
            to_scc = node_to_scc[flowTo[edge_step]]
            if from_scc != to_scc:
                scc_map[from_scc].append(to_scc)
            edge_step += 1

        degree_in = [0] * len(strongly_connected_components)
        scc_idx = 0
        while scc_idx < len(strongly_connected_components):
            for linked_scc in scc_map[scc_idx]:
                degree_in[linked_scc] += 1
            scc_idx += 1

        rune_additions = 0
        check_idx = 0
        while check_idx < len(strongly_connected_components):
            if degree_in[check_idx] == 0 and not crystal_flags[check_idx]:
                rune_additions += 1
            check_idx += 1

        return rune_additions