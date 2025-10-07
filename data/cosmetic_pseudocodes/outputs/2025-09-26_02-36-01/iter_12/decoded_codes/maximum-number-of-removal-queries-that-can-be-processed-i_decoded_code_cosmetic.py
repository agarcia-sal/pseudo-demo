from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            countTracker = 0
            pointer = 0
            while pointer < len(subseq):
                currentQueryIndex = 0
                while currentQueryIndex < len(queries):
                    if pointer == len(subseq):
                        break
                    if subseq[pointer] >= queries[currentQueryIndex]:
                        countTracker += 1
                        pointer += 1
                    currentQueryIndex += 1
                break
            return countTracker

        def subsortAscending(arr: List[int]) -> None:
            lengthArr = len(arr)
            idx1 = 0
            while idx1 < lengthArr - 1:
                idx2 = 0
                while idx2 < lengthArr - idx1 - 1:
                    if arr[idx2] > arr[idx2 + 1]:
                        arr[idx2], arr[idx2 + 1] = arr[idx2 + 1], arr[idx2]
                    idx2 += 1
                idx1 += 1

        totalNums = len(nums)
        totalQueries = len(queries)
        maxResult = process_queries(nums, queries)

        iterator = 0
        while True:
            if iterator >= totalNums:
                break

            leftPart = nums[:iterator]
            rightPart = nums[totalNums-1:iterator-1 if iterator > 0 else None:-1]
            combinedList = leftPart + rightPart

            subsortAscending(combinedList)

            candidate = process_queries(combinedList, queries)

            if candidate > maxResult:
                maxResult = candidate

            iterator += 1

        return maxResult