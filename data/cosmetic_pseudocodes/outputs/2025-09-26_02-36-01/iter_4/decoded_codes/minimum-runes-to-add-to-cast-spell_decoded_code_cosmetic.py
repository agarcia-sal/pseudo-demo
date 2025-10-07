from collections import defaultdict

class Solution:
    def minRunesToAdd(self, n, flowFrom, flowTo, crystals):
        connections = defaultdict(list)
        inverse_connections = defaultdict(list)

        idx = 0
        stack_list = []
        on_stack_flag = [False] * n
        discovery_indices = [-1] * n
        low_link_vals = [0] * n
        strongly_connected_components = []

        # Build graph and inverse graph
        for pos in range(len(flowFrom)):
            start_node = flowFrom[pos]
            end_node = flowTo[pos]
            connections[start_node].append(end_node)
            inverse_connections[end_node].append(start_node)

        # Tarjan's Algorithm for SCC
        def tarjan(node):
            nonlocal idx
            discovery_indices[node] = idx
            low_link_vals[node] = idx
            idx += 1
            stack_list.append(node)
            on_stack_flag[node] = True

            neighbors_list = connections.get(node, [])

            for neighbor in neighbors_list:
                if discovery_indices[neighbor] == -1:
                    tarjan(neighbor)
                    if low_link_vals[neighbor] < low_link_vals[node]:
                        low_link_vals[node] = low_link_vals[neighbor]
                elif on_stack_flag[neighbor] and discovery_indices[neighbor] < low_link_vals[node]:
                    low_link_vals[node] = discovery_indices[neighbor]

            if low_link_vals[node] == discovery_indices[node]:
                component = []
                while True:
                    w = stack_list.pop()
                    on_stack_flag[w] = False
                    component.append(w)
                    if w == node:
                        break
                strongly_connected_components.append(component)

        # Run tarjan on all nodes
        for iteration_index in range(n):
            if discovery_indices[iteration_index] == -1:
                tarjan(iteration_index)

        component_graph = defaultdict(list)
        node_to_component = [-1] * n
        component_contains_crystal = [False] * len(strongly_connected_components)
        component_id = 0

        # Assign nodes to components and mark which components have crystals
        for scc_index, comp_nodes in enumerate(strongly_connected_components):
            for vertex in comp_nodes:
                node_to_component[vertex] = component_id
                if vertex in crystals:
                    component_contains_crystal[scc_index] = True
            component_id += 1

        # Build component graph
        for pos in range(len(flowFrom)):
            from_node = flowFrom[pos]
            to_node = flowTo[pos]
            from_component = node_to_component[from_node]
            to_component = node_to_component[to_node]
            if from_component != to_component:
                component_graph[from_component].append(to_component)

        incoming_edge_count = [0] * len(strongly_connected_components)
        for comp_idx in range(len(strongly_connected_components)):
            adj_list = component_graph.get(comp_idx, [])
            for neighbor_component in adj_list:
                incoming_edge_count[neighbor_component] += 1

        rune_additions_needed = 0
        for component_iter in range(len(strongly_connected_components)):
            if incoming_edge_count[component_iter] == 0 and not component_contains_crystal[component_iter]:
                rune_additions_needed += 1

        return rune_additions_needed