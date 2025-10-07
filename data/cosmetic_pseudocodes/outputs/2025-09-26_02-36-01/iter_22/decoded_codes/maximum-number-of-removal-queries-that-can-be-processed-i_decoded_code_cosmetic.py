from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            counter = 0
            iterator = 0
            while iterator < len(subseq):
                if not (counter < len(queries)):
                    break
                if subseq[iterator] >= queries[counter]:
                    counter += 1
                iterator += 1
            return counter

        length_nums = len(nums)
        processed_maximum = process_queries(nums, queries)

        for index in range(length_nums):
            segment_start = nums[:index]
            segment_end = nums[index:]
            reversed_end = []
            pos = len(segment_end) - 1
            while pos >= 0:
                reversed_end.append(segment_end[pos])
                pos -= 1
            concatenated_subseq = segment_start + reversed_end

            sorted_subsequence = concatenated_subseq.copy()

            def sort_ascending(L: List[int]) -> None:
                swapped = True
                while swapped:
                    swapped = False
                    for idx in range(len(L) - 1):
                        if L[idx] > L[idx + 1]:
                            L[idx], L[idx + 1] = L[idx + 1], L[idx]
                            swapped = True

            sort_ascending(sorted_subsequence)

            current_processed = process_queries(sorted_subsequence, queries)
            if current_processed > processed_maximum:
                processed_maximum = current_processed

        return processed_maximum