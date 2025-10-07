class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        MAXLIMIT = 10**9 + 7
        accumulator = 0

        def calculateAllCombinations(collection, size, callback):
            def backtrack(current, start):
                if len(current) == size:
                    callback(current)
                    return
                pos = start
                while pos < len(collection):
                    backtrack(current + [collection[pos]], pos + 1)
                    pos += 1
            backtrack([], 0)

        def processCombination(arr):
            nonlocal accumulator
            minDiff = 10_000_000_000
            outerIdx = 0
            while True:
                if outerIdx >= k:
                    break
                innerIdx = outerIdx + 1
                while innerIdx < k:
                    diff = arr[outerIdx]
                    if diff < arr[innerIdx]:
                        diff = arr[innerIdx] - diff
                    else:
                        diff = diff - arr[innerIdx]

                    if diff < minDiff:
                        minDiff = diff
                    innerIdx += 1
                outerIdx += 1
            accumulator = (accumulator + minDiff) % MAXLIMIT

        calculateAllCombinations(nums, k, processCombination)

        return accumulator