from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            current_index = 0
            output_count = 0
            while output_count < len(subseq) and current_index < len(queries):
                current_element = subseq[output_count]
                current_query = queries[current_index]
                if not (current_element < current_query):
                    output_count += 1
                current_index += 1
            return output_count

        total_length = len(nums)
        maximum_result = process_queries(nums, queries)

        for iterator in range(total_length):
            head_segment = nums[:iterator]
            tail_segment = nums[iterator:]
            reversed_tail = tail_segment[::-1]

            combined_sequence = head_segment + reversed_tail

            def ascending_compare(x: int, y: int) -> bool:
                return x <= y

            def swap_if_needed(arr: List[int], index_a: int, index_b: int):
                if not ascending_compare(arr[index_a], arr[index_b]):
                    arr[index_a], arr[index_b] = arr[index_b], arr[index_a]

            changed = True
            while changed:
                changed = False
                for j in range(len(combined_sequence) - 1):
                    swap_if_needed(combined_sequence, j, j + 1)
                    if not ascending_compare(combined_sequence[j], combined_sequence[j + 1]):
                        changed = True

            current_max = process_queries(combined_sequence, queries)
            if maximum_result < current_max:
                maximum_result = current_max

        return maximum_result