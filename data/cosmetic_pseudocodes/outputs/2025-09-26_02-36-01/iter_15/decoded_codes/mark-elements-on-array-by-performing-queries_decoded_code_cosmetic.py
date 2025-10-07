from typing import List, Optional, Tuple

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def reheapify(lst: List[List[int]]) -> None:
            length_counter = len(lst)
            parent_idx = (length_counter // 2) - 1
            while parent_idx >= 0:
                child_idx = 2 * parent_idx + 1
                current_idx = parent_idx
                while child_idx < length_counter:
                    right_child_idx = child_idx + 1
                    if right_child_idx < length_counter and lst[right_child_idx][0] < lst[child_idx][0]:
                        child_idx = right_child_idx
                    if lst[current_idx][0] > lst[child_idx][0]:
                        lst[current_idx], lst[child_idx] = lst[child_idx], lst[current_idx]
                        current_idx = child_idx
                        child_idx = 2 * current_idx + 1
                    else:
                        break
                parent_idx -= 1

        def pop_heap(heap_list: List[List[int]]) -> Optional[List[int]]:
            size_val = len(heap_list)
            if size_val == 0:
                return None
            popped_element = heap_list[0]
            heap_list[0] = heap_list[size_val - 1]
            heap_list.pop()
            idx_pointer = 0
            length_heap = len(heap_list)
            while True:
                left_child = 2 * idx_pointer + 1
                right_child = 2 * idx_pointer + 2
                smallest_idx = idx_pointer
                if left_child < length_heap and heap_list[left_child][0] < heap_list[smallest_idx][0]:
                    smallest_idx = left_child
                if right_child < length_heap and heap_list[right_child][0] < heap_list[smallest_idx][0]:
                    smallest_idx = right_child
                if smallest_idx != idx_pointer:
                    heap_list[idx_pointer], heap_list[smallest_idx] = heap_list[smallest_idx], heap_list[idx_pointer]
                    idx_pointer = smallest_idx
                else:
                    break
            return popped_element

        heap_storage: List[List[int]] = []
        num_size = len(nums)
        enum_pointer = 0
        while enum_pointer < num_size:
            element_val = nums[enum_pointer]
            heap_storage.append([element_val, enum_pointer])
            enum_pointer += 1

        reheapify(heap_storage)

        visited_indices = set()
        sum_total = 0
        pos_pointer = 0
        while pos_pointer < num_size:
            sum_total += nums[pos_pointer]
            pos_pointer += 1

        output_list = []
        q_index = 0
        q_size = len(queries)
        while q_index < q_size:
            query_pair = queries[q_index]
            first_idx = query_pair[0]
            second_val = query_pair[1]

            if first_idx not in visited_indices:
                visited_indices.add(first_idx)
                sum_total -= nums[first_idx]

            counter_internal = 0
            while counter_internal < second_val and len(heap_storage) > 0:
                min_pair = pop_heap(heap_storage)
                if min_pair is None:
                    break
                val_extracted, idx_extracted = min_pair
                if idx_extracted not in visited_indices:
                    visited_indices.add(idx_extracted)
                    sum_total -= val_extracted
                    counter_internal += 1

            output_list.append(sum_total)
            q_index += 1

        return output_list