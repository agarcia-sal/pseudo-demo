from collections import defaultdict

class Solution:
    def maximumSubtreeSize(self, edges, colors):
        connection_map = defaultdict(list)

        def populate_edges(idx):
            if idx >= len(edges):
                return
            first_node = edges[idx][0]
            second_node = edges[idx][1]
            connection_map[first_node].append(second_node)
            connection_map[second_node].append(first_node)
            populate_edges(idx + 1)

        populate_edges(0)

        maximum_size = 1

        def dfs(current_node, parent_node):
            nonlocal maximum_size
            count_with_same_color = 1
            children_have_all_same_color = True

            neighbor_index = len(connection_map[current_node]) - 1
            while neighbor_index >= 0:
                adjacent_node = connection_map[current_node][neighbor_index]
                if adjacent_node != parent_node:
                    subtree_size = dfs(adjacent_node, current_node)
                    if subtree_size == 0:
                        children_have_all_same_color = False
                    else:
                        if colors[adjacent_node] == colors[current_node]:
                            count_with_same_color += subtree_size
                        else:
                            children_have_all_same_color = False
                neighbor_index -= 1

            if children_have_all_same_color:
                if maximum_size < count_with_same_color:
                    maximum_size = count_with_same_color
                return count_with_same_color
            else:
                return 0

        start_node = 0
        no_parent_marker = -1
        dfs(start_node, no_parent_marker)
        return maximum_size