from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        modulus = 10_000_000_7

        mapF = defaultdict(int)
        mapG = defaultdict(int)

        def helperIncrement(m, k, val):
            m[k] = (m[k] + val) % modulus

        def processAtIndex(index):
            if index == len(nums):
                return
            currentNum = nums[index]

            helperIncrement(mapG, currentNum, 1)
            helperIncrement(mapF, currentNum, currentNum)

            tempF1 = (mapF[currentNum - 1] + mapF[currentNum] + ((mapG[currentNum - 1] * currentNum) % modulus)) % modulus
            mapF[currentNum] = tempF1

            tempG1 = (mapG[currentNum] + mapG[currentNum - 1]) % modulus
            mapG[currentNum] = tempG1

            tempF2 = (mapF[currentNum] + mapF[currentNum + 1] + ((mapG[currentNum + 1] * currentNum) % modulus)) % modulus
            mapF[currentNum] = tempF2

            tempG2 = (mapG[currentNum] + mapG[currentNum + 1]) % modulus
            mapG[currentNum] = tempG2

            processAtIndex(index + 1)

        processAtIndex(0)

        valuesF = list(mapF.values())
        accSum = 0
        idx = len(valuesF) - 1
        while idx >= 0:
            accSum += valuesF[idx]
            idx -= 1

        return accSum % modulus