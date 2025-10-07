class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        def ToBinaryString(value: int, length: int) -> str:
            result = ""
            counter = length
            while counter > 0:
                bitVal = value % 2
                value //= 2
                result = str(bitVal) + result
                counter -= 1
            while len(result) < length:
                result = "0" + result
            return result

        tempList = [ToBinaryString(num, m) for num in nums]

        def hamming_distance(bin1: str, bin2: str) -> int:
            distVal = 0
            pos = 0
            while pos < len(bin1):
                if bin1[pos] != bin2[pos]:
                    distVal += 1
                pos += 1
            return distVal

        output = []
        outerIndex = 0
        while outerIndex < len(nums):
            currMax = 0
            innerIndex = 0
            while innerIndex < len(nums):
                if outerIndex != innerIndex:
                    d = hamming_distance(tempList[outerIndex], tempList[innerIndex])
                    if d > currMax:
                        currMax = d
                innerIndex += 1
            output.append(currMax)
            outerIndex += 1

        return output