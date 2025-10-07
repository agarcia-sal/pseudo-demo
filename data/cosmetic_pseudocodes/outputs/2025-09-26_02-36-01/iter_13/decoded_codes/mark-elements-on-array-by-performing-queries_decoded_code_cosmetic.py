class Solution:
    def unmarkedSumArray(self, nums, queries):
        epsilon = 0
        delta = 1
        omega_stack = []
        alpha_set = set()
        gamma_value = 0
        beta_list = []

        def heapifyLocal(h):
            heap_size = len(h)
            i = heap_size // 2 - delta
            while i >= epsilon:
                j = i
                while 2 * j + delta < heap_size:
                    left_child = 2 * j + delta
                    right_child = left_child + delta
                    smallest = j
                    if h[left_child][0] < h[smallest][0]:
                        smallest = left_child
                    if right_child < heap_size and h[right_child][0] < h[smallest][0]:
                        smallest = right_child
                    if smallest != j:
                        h[j], h[smallest] = h[smallest], h[j]
                        j = smallest
                    else:
                        break
                i -= delta

        def heappopLocal(h):
            ret_val = h[epsilon]
            h[epsilon] = h[-delta]
            h.pop()
            if h:
                heapifyLocal(h)
            return ret_val

        gamma_value = epsilon
        while gamma_value < len(nums):
            omega_stack.append((nums[gamma_value], gamma_value))
            gamma_value += delta

        heapifyLocal(omega_stack)

        sum_accum = epsilon
        gamma_value = epsilon
        while gamma_value < len(nums):
            sum_accum += nums[gamma_value]
            gamma_value += delta

        gamma_value = epsilon
        while gamma_value < len(queries):
            current_index = queries[gamma_value][0]
            current_k = queries[gamma_value][1]

            if current_index not in alpha_set:
                alpha_set.add(current_index)
                sum_accum -= nums[current_index]

            popped_count = epsilon
            while popped_count < current_k and len(omega_stack) != epsilon:
                val_idx_pair = heappopLocal(omega_stack)
                local_value = val_idx_pair[0]
                local_index = val_idx_pair[1]

                if local_index not in alpha_set:
                    alpha_set.add(local_index)
                    sum_accum -= local_value
                    popped_count += delta

            beta_list.append(sum_accum)
            gamma_value += delta

        return beta_list