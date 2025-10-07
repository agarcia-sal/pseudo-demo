class Solution:
    def maxHammingDistances(self, originalList: list[int], length_m: int) -> list[int]:
        def toBinaryWithPadding(value: int, width: int) -> str:
            def intToBinary(val: int) -> str:
                if val == 0:
                    return "0"
                binStr = ""
                currVal = val
                while currVal > 0:
                    bit_char = "1" if (currVal % 2) == 1 else "0"
                    binStr = bit_char + binStr
                    currVal //= 2
                return binStr

            baseBinary = intToBinary(value)
            paddingLen = width - len(baseBinary)
            zeros = ""
            count_p = 0
            while count_p < paddingLen:
                zeros += "0"
                count_p += 1
            return zeros + baseBinary

        encodedNums = []
        idx_a = 0
        while idx_a < len(originalList):
            val_a = originalList[idx_a]
            encodedNums.append(toBinaryWithPadding(val_a, length_m))
            idx_a += 1

        resultList = []

        def computeHammingDistance(textA: str, textB: str) -> int:
            distCount = 0
            pos = 0
            while pos < len(textA):
                if textA[pos] != textB[pos]:
                    distCount += 1
                pos += 1
            return distCount

        outer = 0
        while True:
            if outer >= len(encodedNums):
                break
            currentMax = 0
            inner = 0
            while True:
                if inner >= len(encodedNums):
                    break
                if outer != inner:
                    distComp = computeHammingDistance(encodedNums[outer], encodedNums[inner])
                    if distComp > currentMax:
                        currentMax = distComp
                inner += 1
            resultList.append(currentMax)
            outer += 1

        return resultList