class Solution:
    def bfs(self, graph, start):
        size = len(graph)
        marked = [False] * size
        items = []
        self.enqueueLeft(items, (start, 0))
        self.setTrue(marked, start)
        far_node = start
        max_dist = 0

        def dequeProcess():
            nonlocal far_node, max_dist
            if len(items) == 0:
                return
            cur = self.dequeueLeft(items)
            current_node = cur[0]
            current_dist = cur[1]

            if current_dist > max_dist:
                max_dist = current_dist
                far_node = current_node

            neighbor_index = len(graph[current_node]) - 1
            while neighbor_index >= 0:
                nxt_neigh = graph[current_node][neighbor_index]
                if not marked[nxt_neigh]:
                    self.setTrue(marked, nxt_neigh)
                    self.enqueueLeft(items, (nxt_neigh, current_dist + 1))
                neighbor_index -= 1

            dequeProcess()

        dequeProcess()
        return far_node, max_dist

    def tree_diameter(self, graph):
        root_node = 0
        temp_far, _unused1 = self.bfs(graph, root_node)
        _unused2, dia = self.bfs(graph, temp_far)
        return dia

    def maximum_path_length_from_node(self, graph, node):
        graph_len = len(graph)
        visit_flags = [False] * graph_len
        deq_list = []
        self.enqueueLeft(deq_list, (node, 0))
        self.setTrue(visit_flags, node)
        max_dist_val = 0

        def processDeque():
            nonlocal max_dist_val
            if len(deq_list) == 0:
                return
            elem = self.dequeueLeft(deq_list)
            current_n = elem[0]
            current_dist2 = elem[1]

            if current_dist2 > max_dist_val:
                max_dist_val = current_dist2

            idx_neigh = len(graph[current_n]) - 1
            while True:
                if idx_neigh < 0:
                    break
                neighb = graph[current_n][idx_neigh]
                if not visit_flags[neighb]:
                    self.setTrue(visit_flags, neighb)
                    self.enqueueLeft(deq_list, (neighb, current_dist2 + 1))
                idx_neigh -= 1

            processDeque()

        processDeque()
        return max_dist_val

    def minimumDiameterAfterMerge(self, edges1, edges2):
        len_g1 = len(edges1) + 1
        len_g2 = len(edges2) + 1

        tree1 = [[] for _ in range(len_g1)]
        tree2 = [[] for _ in range(len_g2)]

        idx1 = len(edges1) - 1
        while idx1 >= 0:
            pair1 = edges1[idx1]
            u1 = pair1[0]
            v1 = pair1[1]
            self.appendToList(tree1[u1], v1)
            self.appendToList(tree1[v1], u1)
            idx1 -= 1

        idx2 = len(edges2) - 1
        while idx2 >= 0:
            pair2 = edges2[idx2]
            u2 = pair2[0]
            v2 = pair2[1]
            self.appendToList(tree2[u2], v2)
            self.appendToList(tree2[v2], u2)
            idx2 -= 1

        dia_one = self.tree_diameter(tree1)
        dia_two = self.tree_diameter(tree2)

        longest_in_1 = []
        count1 = len_g1 - 1
        while count1 >= 0:
            self.appendToList(longest_in_1, self.maximum_path_length_from_node(tree1, count1))
            count1 -= 1

        longest_in_2 = []
        count2 = len_g2 - 1
        while count2 >= 0:
            self.appendToList(longest_in_2, self.maximum_path_length_from_node(tree2, count2))
            count2 -= 1

        smallest_diameter = float('inf')

        i_pos = 0
        while i_pos <= len_g1 - 1:
            j_pos = 0
            while j_pos <= len_g2 - 1:
                candidate_dia = dia_one
                if dia_two > candidate_dia:
                    candidate_dia = dia_two
                path_sum = longest_in_1[i_pos] + longest_in_2[j_pos] + 1
                if path_sum > candidate_dia:
                    candidate_dia = path_sum
                if candidate_dia < smallest_diameter:
                    smallest_diameter = candidate_dia
                j_pos += 1
            i_pos += 1

        return smallest_diameter

    def enqueueLeft(self, list_ref, item):
        self.insertAt(list_ref, 0, item)

    def dequeueLeft(self, list_ref):
        removed_item = list_ref[0]
        self.removeAtIndex(list_ref, 0)
        return removed_item

    def setTrue(self, arr_ref, idx):
        arr_ref[idx] = True

    def appendToList(self, lst, val):
        self.insertAt(lst, len(lst), val)

    def insertAt(self, lst, pos, val):
        length_before = len(lst)
        k = length_before
        while k > pos:
            if k == length_before:
                lst.append(None)
            lst[k] = lst[k - 1]
            k -= 1
        lst[pos] = val

    def removeAtIndex(self, lst, pos):
        len_now = len(lst)
        z = pos
        while z < len_now - 1:
            lst[z] = lst[z + 1]
            z += 1
        lst.pop()