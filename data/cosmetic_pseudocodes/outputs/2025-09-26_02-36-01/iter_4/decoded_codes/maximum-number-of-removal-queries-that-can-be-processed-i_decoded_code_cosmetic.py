from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            pos = 0
            idx = 0
            length_subseq = len(subseq)
            length_queries = len(queries)
            while idx < length_queries:
                if pos == length_subseq:
                    break
                current_element = subseq[pos]
                if current_element >= queries[idx]:
                    pos += 1
                idx += 1
            return pos

        length_nums = len(nums)
        maximum_processed = process_queries(nums, queries)

        for count in range(length_nums):
            start_sublist = nums[:count]
            end_sublist = nums[length_nums - 1:count - 1:-1] if count != 0 else nums[::-1]

            combined_sublist = start_sublist + end_sublist
            sorted_sublist = combined_sublist[:]

            # Selection sort as per pseudocode
            n = len(sorted_sublist)
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if sorted_sublist[i] > sorted_sublist[j]:
                        sorted_sublist[i], sorted_sublist[j] = sorted_sublist[j], sorted_sublist[i]

            processed_count = process_queries(sorted_sublist, queries)
            if processed_count > maximum_processed:
                maximum_processed = processed_count

        return maximum_processed