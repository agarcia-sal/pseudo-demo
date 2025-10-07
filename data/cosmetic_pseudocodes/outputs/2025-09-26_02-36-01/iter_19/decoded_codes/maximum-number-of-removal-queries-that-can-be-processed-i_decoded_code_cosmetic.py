from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            z = 0
            idx = 0
            while idx < len(queries):
                if z == len(subseq):
                    break
                if subseq[z] >= queries[idx]:
                    z += 1
                idx += 1
            return z

        lenNums = len(nums)
        maxCount = process_queries(nums, queries)

        for counter in range(lenNums):
            frontPart = nums[:counter]
            backPart = nums[lenNums - 1:counter - 1 if counter > 0 else None:-1]
            candidateSeq = frontPart + backPart

            # Insertion sort of candidateSeq
            for m in range(1, len(candidateSeq)):
                keyVal = candidateSeq[m]
                l = m - 1
                while l >= 0 and candidateSeq[l] > keyVal:
                    candidateSeq[l + 1] = candidateSeq[l]
                    l -= 1
                candidateSeq[l + 1] = keyVal

            processed = process_queries(candidateSeq, queries)
            if processed > maxCount:
                maxCount = processed

        return maxCount