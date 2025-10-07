import heapq
from typing import List, Tuple, Optional, Set

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        def push_all(heap: List[Tuple[int, int]], elements: List[Tuple[int, int]]) -> None:
            # Recursively push all elements into the heap
            idx = 0
            def push_element():
                nonlocal idx
                if idx < len(elements):
                    heap.append(elements[idx])
                    idx += 1
                    push_element()
            push_element()

        def pop_valid(heap: List[Tuple[int, int]], excluded_set: Set[int]) -> Tuple[Optional[int], Optional[int]]:
            # Pop elements from heap until we find one not in excluded_set or heap is empty
            while heap:
                val, idx = heapq.heappop(heap)
                if idx not in excluded_set:
                    return val, idx
            return None, None

        container_heap: List[Tuple[int, int]] = []
        elements_list = [(nums[i], i) for i in range(len(nums))]
        push_all(container_heap, elements_list)
        heapq.heapify(container_heap)

        excluded_indices: Set[int] = set()
        summation = sum(nums)
        result_list: List[int] = []

        for pos_index, k_val in queries:
            if pos_index not in excluded_indices:
                excluded_indices.add(pos_index)
                summation -= nums[pos_index]

            counter = 0
            continue_loop = True
            while continue_loop:
                if counter >= k_val or not container_heap:
                    continue_loop = False
                else:
                    val_popped, idx_popped = pop_valid(container_heap, excluded_indices)
                    if idx_popped is None:
                        continue_loop = False
                    else:
                        excluded_indices.add(idx_popped)
                        summation -= val_popped
                        counter += 1

            result_list.append(summation)

        return result_list