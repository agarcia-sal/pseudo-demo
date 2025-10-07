class Solution:
    def maxTotalReward(self, rewardValues):
        auxiliary = 1
        sortedUniqueValues = []

        while True:
            if not rewardValues:
                break
            minElem = rewardValues[0]
            for element in rewardValues:
                if element < minElem:
                    minElem = element
            if minElem not in sortedUniqueValues:
                sortedUniqueValues.append(minElem)
            filtered = []
            for elem in rewardValues:
                if elem != minElem:
                    filtered.append(elem)
            rewardValues = filtered

        index = 0
        while index < len(sortedUniqueValues):
            currentValue = sortedUniqueValues[index]
            shiftLeftVal = (1 << currentValue) - 1
            combinedShift = shiftLeftVal << currentValue
            bitwiseAndRes = auxiliary & combinedShift
            auxiliary = auxiliary | bitwiseAndRes
            index += 1

        bitCount = 0
        tempVal = auxiliary
        while tempVal > 0:
            tempVal >>= 1
            bitCount += 1

        return bitCount - 1