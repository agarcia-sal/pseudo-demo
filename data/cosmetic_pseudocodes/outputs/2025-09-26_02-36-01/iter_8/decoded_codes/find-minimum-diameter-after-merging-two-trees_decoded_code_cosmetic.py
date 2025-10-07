class Solution:
    def bfs(self, graph, start):
        count = len(graph)
        mask = [False] * count

        def enqueue(item):
            nonlocal queue
            queue.append(item)

        queue = [(start, 0)]
        idx = 0
        mask[start] = True
        node_far = start
        dist_max = 0

        while True:
            if idx >= len(queue):
                return node_far, dist_max
            current_pair = queue[idx]
            idx += 1
            node_ite, dist_ite = current_pair

            if dist_ite > dist_max:
                dist_max = dist_ite
                node_far = node_ite

            nbr_coll = graph[node_ite]
            pos_ind = 0
            while pos_ind < len(nbr_coll):
                nbr = nbr_coll[pos_ind]
                if not mask[nbr]:
                    mask[nbr] = True
                    enqueue((nbr, dist_ite + 1))
                pos_ind += 1

    def tree_diameter(self, graph):
        start_node = 0
        far_node, _ = self.bfs(graph, start_node)
        _, diam = self.bfs(graph, far_node)
        return diam

    def maximum_path_length_from_node(self, graph, node):
        size = len(graph)
        seen = [False] * size
        backing_queue = [(node, 0)]
        index_pos = 0
        seen[node] = True
        max_len = 0

        while True:
            if index_pos >= len(backing_queue):
                return max_len
            pair_cur = backing_queue[index_pos]
            index_pos += 1
            curr_node, curr_dist = pair_cur

            if curr_dist > max_len:
                max_len = curr_dist

            neighbors_list = graph[curr_node]
            place = 0
            while place < len(neighbors_list):
                nb = neighbors_list[place]
                if not seen[nb]:
                    seen[nb] = True
                    new_dist = curr_dist + 1
                    backing_queue.append((nb, new_dist))
                place += 1

    def minimumDiameterAfterMerge(self, edges1, edges2):
        length_n = len(edges1) + 1
        length_m = len(edges2) + 1

        gph1 = [[] for _ in range(length_n)]
        gph2 = [[] for _ in range(length_m)]

        for edge_curr in edges1:
            u_e, v_e = edge_curr
            gph1[u_e].append(v_e)
            gph1[v_e].append(u_e)

        for edge_cur in edges2:
            u_e2, v_e2 = edge_cur
            gph2[u_e2].append(v_e2)
            gph2[v_e2].append(u_e2)

        dia1 = self.tree_diameter(gph1)
        dia2 = self.tree_diameter(gph2)

        longest_paths_1 = [self.maximum_path_length_from_node(gph1, i) for i in range(length_n)]
        longest_paths_2 = [self.maximum_path_length_from_node(gph2, j) for j in range(length_m)]

        inf_val = float("inf")
        min_diam = inf_val

        idx_u = 0
        while idx_u < length_n:
            idx_v = 0
            while idx_v < length_m:
                combined_max1 = dia1
                combined_max2 = dia2
                combined_len = longest_paths_1[idx_u] + longest_paths_2[idx_v] + 1
                trio_max = combined_max1
                if combined_max2 > trio_max:
                    trio_max = combined_max2
                if combined_len > trio_max:
                    trio_max = combined_len
                if trio_max < min_diam:
                    min_diam = trio_max
                idx_v += 1
            idx_u += 1

        return min_diam