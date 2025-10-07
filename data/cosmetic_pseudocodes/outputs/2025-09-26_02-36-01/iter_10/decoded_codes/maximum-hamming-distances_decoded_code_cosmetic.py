class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        collectedStrings = []

        def toBinary(n: int, length: int) -> str:
            bits = []

            def innerConvert(x: int, rem: int) -> None:
                if rem == 0:
                    return
                innerConvert(x // 2, rem - 1)
                bits.append(str(x % 2))

            innerConvert(n, length)
            return ''.join(bits)

        idx1 = 0
        while idx1 < len(nums):
            collectedStrings.append(toBinary(nums[idx1], m))
            idx1 += 1

        results = []

        def hamming_distance(binX: str, binY: str) -> int:
            count_mismatches = 0
            for pos in range(len(binX)):
                if binX[pos] != binY[pos]:
                    count_mismatches += 1
            return count_mismatches

        outerIndex = 0
        while outerIndex < len(nums):
            current_max = 0
            innerIndex = 0
            while innerIndex < len(nums):
                if outerIndex != innerIndex:
                    distVal = hamming_distance(collectedStrings[outerIndex], collectedStrings[innerIndex])
                    if distVal > current_max:
                        current_max = distVal
                innerIndex += 1
            results.append(current_max)
            outerIndex += 1

        return results