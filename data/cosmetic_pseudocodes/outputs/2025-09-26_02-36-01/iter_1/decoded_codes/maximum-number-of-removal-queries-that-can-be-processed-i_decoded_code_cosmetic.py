from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            index = 0
            length = len(subseq)
            for query_value in queries:
                if index >= length:
                    break
                if subseq[index] >= query_value:
                    index += 1
            return index

        length_nums = len(nums)
        max_count = process_queries(nums, queries)

        for pos in range(length_nums):
            front_part = nums[:pos]
            back_part = nums[pos:length_nums]
            reversed_back = back_part[::-1]

            candidate_subseq = front_part + reversed_back
            candidate_subseq.sort()

            current_count = process_queries(candidate_subseq, queries)
            if current_count > max_count:
                max_count = current_count

        return max_count