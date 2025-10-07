class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        binReprs = []
        idxOuter = 0
        base = 2  # derived from (2 + 2) / 2
        one = 1
        zero = 0
        step = 1  # derived from (3 - 2)

        # Convert each number in nums to a binary string of length m
        while idxOuter < len(nums):
            numVal = nums[idxOuter]
            padLen = m
            tmpBinStr = ""
            valCopy = numVal
            while valCopy > zero:
                remBit = valCopy % base
                remChar = "1" if remBit == one else "0"
                tmpBinStr = remChar + tmpBinStr
                valCopy //= base
            charsNeeded = padLen - len(tmpBinStr)
            padStr = "0" * charsNeeded
            fullBinStr = padStr + tmpBinStr
            binReprs.append(fullBinStr)
            idxOuter += step

        resultList = []

        def hamming_distance(bin1: str, bin2: str) -> int:
            countDiff = 0
            position = 0
            length = len(bin1)
            while position < length:
                isEqual = bin1[position] == bin2[position]
                if not isEqual:
                    countDiff += step
                position += step
            return countDiff

        idxOuter2 = 0
        while True:
            if idxOuter2 >= len(nums):
                break
            bestDist = 0
            idxInner = 0
            while True:
                if idxInner >= len(nums):
                    break
                if idxOuter2 != idxInner:
                    currDist = hamming_distance(binReprs[idxOuter2], binReprs[idxInner])
                    if currDist > bestDist:
                        bestDist = currDist
                idxInner += step
            resultList.append(bestDist)
            idxOuter2 += step

        return resultList