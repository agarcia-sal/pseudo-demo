from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        MOD_VAL = 10**9 + 7
        dictF = defaultdict(int)
        dictG = defaultdict(int)

        def incrementDictKeyByOne(d, k):
            d[k] += 1

        def computeMod(value):
            return value % MOD_VAL

        def safeGet(d, k):
            return d[k] if k in d else 0

        def processElement(i):
            current = nums[i]

            incrementDictKeyByOne(dictG, current)
            incrementDictKeyByOne(dictF, current)

            dictF[current] = dictF[current] + current - 1
            dictF[current] = dictF[current] + safeGet(dictF, current - 1) + (safeGet(dictG, current - 1) * current)
            dictF[current] = computeMod(dictF[current])

            dictG[current] = dictG[current] + safeGet(dictG, current - 1)
            dictG[current] = computeMod(dictG[current])

            dictF[current] = dictF[current] + safeGet(dictF, current + 1) + (safeGet(dictG, current + 1) * current)
            dictF[current] = computeMod(dictF[current])

            dictG[current] = dictG[current] + safeGet(dictG, current + 1)
            dictG[current] = computeMod(dictG[current])

        def loopOverNums(index):
            if index >= len(nums):
                return
            processElement(index)
            loopOverNums(index + 1)

        loopOverNums(0)

        def sumValues(mapArg):
            keyList = list(mapArg.keys())
            accumulator = 0

            def recursiveSum(arrIndex):
                nonlocal accumulator
                if arrIndex >= len(keyList):
                    return accumulator
                accumulator += mapArg[keyList[arrIndex]]
                return recursiveSum(arrIndex + 1)

            return recursiveSum(0)

        totalSum = sumValues(dictF)
        finalResult = totalSum % MOD_VAL
        return finalResult