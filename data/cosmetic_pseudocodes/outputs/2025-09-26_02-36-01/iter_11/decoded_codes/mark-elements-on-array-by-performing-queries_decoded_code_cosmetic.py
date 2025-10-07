class Solution:
    def unmarkedSumArray(self, nums, queries):
        def ExtractMin(H):
            # Heap pop root and bubble down
            size_inner = len(H)
            if size_inner == 0:
                return None, None
            idx_inner = 0
            val_inner = 0
            parent_idx = 0

            # Replace root with last element before bubble down
            val_inner, idx_inner = H[0]
            H[0] = H[-1]
            H.pop()
            size_inner -= 1

            while parent_idx * 2 + 1 < size_inner:
                child_idx = parent_idx * 2 + 1
                if child_idx + 1 < size_inner and H[child_idx + 1][0] < H[child_idx][0]:
                    child_idx += 1
                if H[parent_idx][0] <= H[child_idx][0]:
                    break
                H[parent_idx], H[child_idx] = H[child_idx], H[parent_idx]
                parent_idx = child_idx
            return val_inner, idx_inner

        def BuildHeap(H):
            length_heap = len(H)
            i_heap = (length_heap // 2) - 1
            while i_heap >= 0:
                parent_pos = i_heap
                while parent_pos * 2 + 1 < length_heap:
                    child_pos = parent_pos * 2 + 1
                    if child_pos + 1 < length_heap and H[child_pos + 1][0] < H[child_pos][0]:
                        child_pos += 1
                    if H[parent_pos][0] <= H[child_pos][0]:
                        break
                    H[parent_pos], H[child_pos] = H[child_pos], H[parent_pos]
                    parent_pos = child_pos
                i_heap -= 1

        heap_container = []
        ic_counter = 0
        n = len(nums)
        while ic_counter < n:
            heap_container.append([nums[ic_counter], ic_counter])
            ic_counter += 1

        BuildHeap(heap_container)

        seen_marks = {}
        total_aggregate = 0
        pos_agg = 0
        while pos_agg < n:
            total_aggregate += nums[pos_agg]
            pos_agg += 1

        final_answer = []
        q_pos = 0
        q_len = len(queries)
        while True:
            if q_pos >= q_len:
                break
            q_idx = queries[q_pos][0]
            q_k = queries[q_pos][1]
            if q_idx not in seen_marks:
                seen_marks[q_idx] = True
                total_aggregate += -nums[q_idx]
            counter_loc = 0
            while counter_loc < q_k and len(heap_container) > 0:
                pop_val, pop_idx = ExtractMin(heap_container)
                if pop_idx is None:
                    break
                if pop_idx not in seen_marks:
                    seen_marks[pop_idx] = True
                    total_aggregate -= pop_val
                    counter_loc += 1
            final_answer.append(total_aggregate)
            q_pos += 1

        return final_answer