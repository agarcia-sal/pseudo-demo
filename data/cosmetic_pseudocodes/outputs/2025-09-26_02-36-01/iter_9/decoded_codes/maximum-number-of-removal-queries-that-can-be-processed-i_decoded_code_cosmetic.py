from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            count = 0
            index = 0
            while index < len(subseq):
                if count == len(queries):
                    break
                if not (subseq[index] < queries[count]):
                    count += 1
                index += 1
            return count

        length_nums = len(nums)
        length_queries = len(queries)
        max_count = process_queries(nums, queries)

        def get_prefix(input_list: List[int], end_idx: int) -> List[int]:
            return input_list[:end_idx]

        def get_suffix(input_list: List[int], start_idx: int) -> List[int]:
            return input_list[start_idx:]

        def reverse_list(lst: List[int]) -> List[int]:
            return lst[::-1]

        def concatenate_lists(a: List[int], b: List[int]) -> List[int]:
            return a + b

        def insertion_sort(arr: List[int]) -> List[int]:
            # In-place insertion sort for clarity
            for i in range(1, len(arr)):
                key_val = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key_val:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key_val
            return arr

        position = 0
        while position < length_nums:
            front_portion = get_prefix(nums, position)
            back_portion = get_suffix(nums, position)
            reversed_back = reverse_list(back_portion)
            joined_list = concatenate_lists(front_portion, reversed_back)
            sorted_subseq = insertion_sort(joined_list[:])  # copy to avoid modifying joined_list
            temp_max = process_queries(sorted_subseq, queries)
            if temp_max > max_count:
                max_count = temp_max
            position += 1

        return max_count