class Solution:
    def numberOfPairs(self, listA, listB, factor):
        def createFrequencyMap(array):
            freq_map = {}
            index = 0
            while index < len(array):
                val = array[index]
                freq_map[val] = freq_map.get(val, 0) + 1
                index += 1
            return freq_map

        frequencyMap = createFrequencyMap(listB)
        totalPairs = 0
        i = 0
        iterKeys = list(frequencyMap.keys())
        while i < len(listA):
            currentValue = listA[i]
            j = 0
            while j < len(iterKeys):
                keyValue = iterKeys[j]
                divisor = keyValue * factor
                # if currentValue % divisor == 0, add frequencyMap[keyValue]
                if divisor != 0 and currentValue % divisor == 0:
                    totalPairs += frequencyMap[keyValue]
                j += 1
            i += 1
        return totalPairs