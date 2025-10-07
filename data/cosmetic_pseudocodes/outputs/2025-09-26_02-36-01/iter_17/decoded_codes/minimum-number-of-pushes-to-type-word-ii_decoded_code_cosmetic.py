class Solution:
    def minimumPushes(self, word: str) -> int:
        tallyMap = {}
        freqEntries = []
        accPushes = 0
        pressCount = 1
        assignedKeys = 0
        idx = 0

        # count frequencies
        while idx < len(word):
            currentChar = word[idx]
            tallyMap[currentChar] = tallyMap.get(currentChar, 0) + 1
            idx += 1

        # extract frequencies into list
        for val in tallyMap.values():
            freqEntries.append(val)

        # bubble sort descending order
        flag = True
        while flag:
            flag = False
            i = 0
            while i < len(freqEntries) - 1:
                if freqEntries[i] < freqEntries[i + 1]:
                    freqEntries[i], freqEntries[i + 1] = freqEntries[i + 1], freqEntries[i]
                    flag = True
                i += 1

        # compute total pushes
        pos = 0
        while True:
            currentFreq = freqEntries[pos]
            accPushes += currentFreq * pressCount
            assignedKeys += 1
            if assignedKeys == 8:
                assignedKeys = 0
                pressCount += 1
            pos += 1
            if pos >= len(freqEntries):
                break

        return accPushes