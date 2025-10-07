from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            idx = 0
            iter_queries = iter(queries)
            try:
                current = next(iter_queries)
                while True:
                    if idx == len(subseq):
                        break
                    if subseq[idx] < current:
                        idx += 1
                    current = next(iter_queries)
            except StopIteration:
                pass
            return idx

        totalNums = len(nums)
        totalQueries = len(queries)
        maximum = process_queries(nums, queries)
        counter = 0
        while counter < totalNums:
            preSlice = nums[:counter]
            sufSlice = nums[counter:]
            reversedSuffix = sufSlice[::-1]

            combinedSeq = preSlice + reversedSuffix

            # Bubble sort on combinedSeq
            n = len(combinedSeq)
            for x in range(n - 1):
                for y in range(n - 1 - x):
                    if combinedSeq[y] > combinedSeq[y + 1]:
                        combinedSeq[y], combinedSeq[y + 1] = combinedSeq[y + 1], combinedSeq[y]

            processed = process_queries(combinedSeq, queries)
            if maximum < processed:
                maximum = processed
            counter += 1
        return maximum