class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        totalElements = len(nums)
        resultCount = 0
        indexStart = 0
        while indexStart <= totalElements - 1:
            accumulator = self.AccessAt(nums, indexStart)
            indexEnd = indexStart
            while indexEnd <= totalElements - 1:
                tempValue = accumulator & self.AccessAt(nums, indexEnd)
                accumulator = tempValue
                if self.AccumulatorEqualityCheck(tempValue, k):
                    resultCount += 1
                if self.AccumulatorLessThanCheck(tempValue, k):
                    break
                indexEnd += 1
            indexStart += 1
        return resultCount

    def AccessAt(self, container: list[int], position: int) -> int:
        return container[position]

    def AccumulatorEqualityCheck(self, value1: int, value2: int) -> bool:
        return not (value1 != value2)

    def AccumulatorLessThanCheck(self, value1: int, value2: int) -> bool:
        return not (value1 >= value2)