from math import inf

class Solution:
    def minimumTime(self, n, edges, disappear):
        alpha = [[] for _ in range(n)]
        for x, y, z in edges:
            alpha[x].append((y, z))
            alpha[y].append((x, z))

        beta = [inf] * n
        beta[0] = 0

        gamma = [(0, 0)]

        def pop_minimum(heap):
            a = heap[0]
            heap[0] = heap[-1]
            heap.pop()
            idx = 0
            while True:
                l_child = 2 * idx + 1
                r_child = 2 * idx + 2
                smallest = idx
                if l_child < len(heap) and heap[l_child][0] < heap[smallest][0]:
                    smallest = l_child
                if r_child < len(heap) and heap[r_child][0] < heap[smallest][0]:
                    smallest = r_child
                if smallest == idx:
                    break
                heap[idx], heap[smallest] = heap[smallest], heap[idx]
                idx = smallest
            return a

        def insert_heap(heap, elem):
            heap.append(elem)
            pos = len(heap) - 1
            while pos > 0:
                parent = (pos - 1) // 2
                if heap[parent][0] <= heap[pos][0]:
                    break
                heap[parent], heap[pos] = heap[pos], heap[parent]
                pos = parent

        while len(gamma) > 0:
            curr_dist, curr_node = pop_minimum(gamma)
            if not (curr_dist < disappear[curr_node]):
                continue
            if not (curr_dist < beta[curr_node]):
                continue

            for neighbor, length in alpha[curr_node]:
                new_dist = curr_dist + length
                if new_dist < beta[neighbor] and new_dist < disappear[neighbor]:
                    beta[neighbor] = new_dist
                    insert_heap(gamma, (new_dist, neighbor))

        final_results = [-1] * n
        idx = 0
        while idx < n:
            if beta[idx] < disappear[idx]:
                final_results[idx] = beta[idx]
            idx += 1

        return final_results