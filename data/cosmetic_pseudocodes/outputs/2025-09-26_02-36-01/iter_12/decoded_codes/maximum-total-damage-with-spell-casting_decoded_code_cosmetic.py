from collections import Counter

class Solution:
    def maximumTotalDamage(self, power):
        def computeMaximum(i, keysList, freqMap, memory):
            if i < 0:
                return 0

            key = keysList[i]
            if key in memory:
                return memory[key]

            currentVal = key * freqMap[key]
            k = i - 1
            while k >= 0 and keysList[k] >= key - 2:
                k -= 1

            including = currentVal + computeMaximum(k, keysList, freqMap, memory)
            excluding = computeMaximum(i - 1, keysList, freqMap, memory)

            answer = max(including, excluding)
            memory[key] = answer
            return answer

        frequency = Counter(power)
        sortedKeys = sorted(frequency)
        memo = {}
        return computeMaximum(len(sortedKeys) - 1, sortedKeys, frequency, memo)