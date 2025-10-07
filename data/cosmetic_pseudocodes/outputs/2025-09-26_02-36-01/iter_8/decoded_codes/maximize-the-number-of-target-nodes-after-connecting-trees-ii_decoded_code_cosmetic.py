from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1, edges2):
        adjacency_map1 = defaultdict(list)
        adjacency_map2 = defaultdict(list)

        for x, y in edges1:
            adjacency_map1[x].append(y)
            adjacency_map1[y].append(x)

        for p, q in edges2:
            adjacency_map2[p].append(q)
            adjacency_map2[q].append(p)

        size_adj1 = len(adjacency_map1)
        size_adj2 = len(adjacency_map2)

        def bfs(graph_structure, origin):
            tally_even = 0
            tally_odd = 0
            exploration_queue = deque([(origin, 1)])
            marked_nodes = {origin}

            while exploration_queue:
                current_node, distance_val = exploration_queue.popleft()
                if distance_val % 2 == 0:
                    tally_even += 1
                else:
                    tally_odd += 1

                for adj_node in graph_structure[current_node]:
                    if adj_node not in marked_nodes:
                        marked_nodes.add(adj_node)
                        exploration_queue.append((adj_node, distance_val + 1))

            return tally_even, tally_odd

        counts_list_1 = []
        iterator_a = 0
        while iterator_a < size_adj1:
            counts_list_1.append(bfs(adjacency_map1, iterator_a))
            iterator_a += 1

        counts_list_2 = []
        iterator_b = 0
        while iterator_b < size_adj2:
            counts_list_2.append(bfs(adjacency_map2, iterator_b))
            iterator_b += 1

        output_collection = []
        outer_index = 0
        while outer_index < size_adj1:
            even1, odd1 = counts_list_1[outer_index]
            local_max = 0
            inner_index = 0
            while inner_index < size_adj2:
                even2, odd2 = counts_list_2[inner_index]
                equal_mod_flag = False
                if outer_index == inner_index:
                    equal_mod_flag = True
                else:
                    if (outer_index % 2) == (inner_index % 2):
                        equal_mod_flag = True

                candidate = even2 if equal_mod_flag else odd2
                if candidate > local_max:
                    local_max = candidate

                inner_index += 1

            output_collection.append(even1 + local_max)
            outer_index += 1

        return output_collection