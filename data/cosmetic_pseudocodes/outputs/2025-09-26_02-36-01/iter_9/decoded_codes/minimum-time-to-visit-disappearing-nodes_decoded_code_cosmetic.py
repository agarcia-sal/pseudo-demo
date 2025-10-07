from collections import defaultdict

class Solution:
    def minimumTime(self, alpha, beta, gamma):
        def push_heap(container, val):
            pos = len(container)
            container.append(val)
            while pos > 0:
                parent_pos = (pos - 1) // 2
                if container[parent_pos][0] <= container[pos][0]:
                    break
                container[pos], container[parent_pos] = container[parent_pos], container[pos]
                pos = parent_pos

        def pop_heap(container):
            if not container:
                return None
            top_element = container[0]
            container[0], container[-1] = container[-1], container[0]
            container.pop()
            idx = 0
            size = len(container)
            while True:
                left_child = 2 * idx + 1
                right_child = 2 * idx + 2
                smallest = idx
                if left_child < size and container[left_child][0] < container[smallest][0]:
                    smallest = left_child
                if right_child < size and container[right_child][0] < container[smallest][0]:
                    smallest = right_child
                if smallest == idx:
                    break
                container[idx], container[smallest] = container[smallest], container[idx]
                idx = smallest
            return top_element

        topology = defaultdict(list)
        for p, q, r in beta:
            topology[p].append((q, r))
            topology[q].append((p, r))

        horizons = [10**15] * alpha
        horizons[0] = 0
        priority_structure = [(0, 0)]

        while priority_structure:
            distance_value, vertex_id = pop_heap(priority_structure)
            if distance_value is None:
                break
            if distance_value >= gamma[vertex_id] or distance_value > horizons[vertex_id]:
                continue
            for adjacent, weight in topology[vertex_id]:
                new_dist = distance_value + weight
                if new_dist < horizons[adjacent] and new_dist < gamma[adjacent]:
                    horizons[adjacent] = new_dist
                    push_heap(priority_structure, (new_dist, adjacent))

        outcome = [-1] * alpha
        index_counter = 0
        while True:
            if index_counter == alpha:
                break
            if horizons[index_counter] < gamma[index_counter]:
                outcome[index_counter] = horizons[index_counter]
            index_counter += 1

        return outcome