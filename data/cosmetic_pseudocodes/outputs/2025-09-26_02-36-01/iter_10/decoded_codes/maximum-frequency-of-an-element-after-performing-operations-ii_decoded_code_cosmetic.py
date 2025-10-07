from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        def addKeyToMap(MAP_A, key, valueToAdd):
            if key not in MAP_A:
                MAP_A[key] = 0
            MAP_A[key] += valueToAdd

        mapAlpha = defaultdict(int)
        mapBeta = defaultdict(int)

        def processIndex(indexItr):
            if indexItr == len(nums):
                return
            curNum = nums[indexItr]

            addKeyToMap(mapAlpha, curNum, 1)
            addKeyToMap(mapBeta, curNum, 0)
            addKeyToMap(mapBeta, curNum - k, 1)
            addKeyToMap(mapBeta, (k + 1) + curNum, -1)

            processIndex(indexItr + 1)

        processIndex(0)

        accumulatorA = 0
        maximumAnswer = 0

        sortedPairs = [(key, mapBeta[key]) for key in mapBeta]
        sortedPairs.sort(key=lambda pair: pair[0])

        def iteratePairs(indexIter):
            nonlocal accumulatorA, maximumAnswer
            if indexIter == len(sortedPairs):
                return

            curKey, curValue = sortedPairs[indexIter]

            accumulatorA += curValue

            tempMin = accumulatorA if accumulatorA < (mapAlpha[curKey] + numOperations) else (mapAlpha[curKey] + numOperations)
            tempMaxCandidate = maximumAnswer if maximumAnswer > tempMin else tempMin

            maximumAnswer = tempMaxCandidate

            iteratePairs(indexIter + 1)

        iteratePairs(0)

        return maximumAnswer