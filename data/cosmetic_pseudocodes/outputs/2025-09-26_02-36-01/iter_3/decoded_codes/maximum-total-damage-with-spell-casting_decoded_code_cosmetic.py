from collections import Counter

class Solution:
    def maximumTotalDamage(self, power):
        freqMap = Counter(power)

        sortedPowers = sorted(freqMap.keys())

        dpMap = {}
        totalEntries = len(sortedPowers)
        idx = 0
        while idx < totalEntries:
            currentVal = sortedPowers[idx]

            optionSkip = 0
            if idx > 0:
                prevVal = sortedPowers[idx - 1]
                optionSkip = dpMap.get(prevVal, 0)

            optionTake = currentVal * freqMap[currentVal]

            prevIndex = idx - 1
            # Decrement prevIndex until sortedPowers[prevIndex] < currentVal - 1
            while prevIndex >= 0 and sortedPowers[prevIndex] >= currentVal - 1:
                prevIndex -= 1

            if prevIndex >= 0:
                optionTake += dpMap[sortedPowers[prevIndex]]

            if optionTake >= optionSkip:
                dpMap[currentVal] = optionTake
            else:
                dpMap[currentVal] = optionSkip

            idx += 1

        bestDamage = 0
        for val in dpMap.values():
            if val > bestDamage:
                bestDamage = val

        return bestDamage