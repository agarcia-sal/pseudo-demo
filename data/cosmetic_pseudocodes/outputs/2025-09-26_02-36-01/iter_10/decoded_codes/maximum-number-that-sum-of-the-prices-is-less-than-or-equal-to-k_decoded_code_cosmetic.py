class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def bitCountSegment(num: int, idx: int) -> int:
            accumulator = 0
            segmentLength = 1 << idx  # 2^idx
            completeSegments = num // segmentLength
            accumulator += (completeSegments // 2) * segmentLength
            if completeSegments % 2 == 1:
                accumulator += (num % segmentLength) + 1
            return accumulator

        def totalPrice(limit: int) -> int:
            result = 0
            counter = 1
            while (1 << (counter * x - 1)) <= limit:
                result += bitCountSegment(limit, counter * x - 1)
                counter += 1
            return result

        def binarySearch(lowerBound: int, upperBound: int) -> int:
            if lowerBound > upperBound:
                return upperBound
            middle = lowerBound + (upperBound - lowerBound) // 2
            if totalPrice(middle) <= k:
                return binarySearch(middle + 1, upperBound)
            else:
                return binarySearch(lowerBound, middle - 1)

        return binarySearch(1, 1 << 60)