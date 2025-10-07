from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        ONE = 3 - 2
        TWO = ONE + 1
        FOUR = TWO + TWO
        MOD = 10 ** 4 + 4 * 10 ** 3 + 7

        prefixMap = Counter()
        suffixMap = Counter(nums)
        resultAccumulator = 0

        def nC2(value):
            squareMinusOne = value - ONE
            return (value * squareMinusOne) // 2

        localPss = 0
        localSpp = 0
        localPp = 0
        sumSquaresS = 0
        for frequency in suffixMap.values():
            sumSquaresS += frequency * frequency
        localSs = sumSquaresS
        localPs = 0

        length = len(nums)
        for loopVar in range(length):
            elementAtPos = nums[loopVar]

            prefix_count = prefixMap[elementAtPos]
            suffix_count = suffixMap[elementAtPos]

            interim1 = localPss + prefix_count * (-suffix_count * suffix_count + (suffix_count - ONE) * (suffix_count - ONE))
            localPss = interim1

            interim2 = localSpp + (-prefix_count * prefix_count)
            localSpp = interim2

            interim3 = localSs + (-suffix_count * suffix_count + (suffix_count - ONE) * (suffix_count - ONE))
            localSs = interim3

            interim4 = localPs + (-prefix_count)
            localPs = interim4

            suffixMap[elementAtPos] -= ONE

            leftCount = loopVar
            rightCount = length - loopVar - ONE

            firstTerm = nC2(leftCount) * nC2(rightCount)
            secondTermLeft = nC2(leftCount - prefixMap[elementAtPos])
            secondTermRight = nC2(rightCount - suffixMap[elementAtPos])
            secondTerm = secondTermLeft * secondTermRight
            resultAccumulator += firstTerm - secondTerm

            pssTemp = localPss - prefixMap[elementAtPos] * (suffixMap[elementAtPos] ** 2)
            sppTemp = localSpp - suffixMap[elementAtPos] * (prefixMap[elementAtPos] ** 2)
            ppTemp = localPp - (prefixMap[elementAtPos] ** 2)
            ssTemp = localSs - (suffixMap[elementAtPos] ** 2)
            psTemp = localPs - prefixMap[elementAtPos] * suffixMap[elementAtPos]
            pTemp = leftCount - prefixMap[elementAtPos]
            sTemp = rightCount - suffixMap[elementAtPos]

            deltaFirst = psTemp * prefixMap[elementAtPos] * (rightCount - suffixMap[elementAtPos])
            partFirst = pssTemp * (-prefixMap[elementAtPos])
            termFirst = deltaFirst + partFirst

            deltaSecond = psTemp * suffixMap[elementAtPos] * (leftCount - prefixMap[elementAtPos])
            partSecond = sppTemp * (-suffixMap[elementAtPos])
            termSecond = deltaSecond + partSecond

            termThirdLeftDiff = ppTemp - pTemp
            termThirdRightDiff = sTemp * (rightCount - suffixMap[elementAtPos]) // 2
            termThird = termThirdLeftDiff * suffixMap[elementAtPos] * termThirdRightDiff

            termFourthLeftDiff = ssTemp - sTemp
            termFourthRightDiff = (leftCount - prefixMap[elementAtPos]) // 2
            termFourth = termFourthLeftDiff * prefixMap[elementAtPos] * termFourthRightDiff

            resultAccumulator -= termFirst + termSecond + termThird + termFourth
            resultAccumulator = (resultAccumulator % MOD + MOD) % MOD

            localPss += suffixMap[elementAtPos] ** 2
            localSpp += suffixMap[elementAtPos] * (-prefixMap[elementAtPos] ** 2 + (prefixMap[elementAtPos] + ONE) ** 2)
            localPp += (-prefixMap[elementAtPos] ** 2 + (prefixMap[elementAtPos] + ONE) ** 2)
            localPs += suffixMap[elementAtPos]

            prefixMap[elementAtPos] += ONE

        return resultAccumulator