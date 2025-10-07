class Solution:
    def maximumTotalDamage(self, power):
        frequencyMap = {}
        for element in power:
            frequencyMap[element] = frequencyMap.get(element, 0) + 1

        distinctValues = sorted(frequencyMap.keys())

        dpMap = {}
        for currentIndex, currentValue in enumerate(distinctValues):
            prevExcluded = dpMap.get(distinctValues[currentIndex - 1], 0) if currentIndex > 0 else 0
            includedSum = currentValue * frequencyMap[currentValue]

            iterator = currentIndex - 1
            while iterator >= 0 and distinctValues[iterator] >= currentValue - 2:
                iterator -= 1

            if iterator >= 0:
                includedSum += dpMap.get(distinctValues[iterator], 0)

            dpMap[currentValue] = includedSum if includedSum > prevExcluded else prevExcluded

        maxResult = max(dpMap.values(), default=0)
        return maxResult