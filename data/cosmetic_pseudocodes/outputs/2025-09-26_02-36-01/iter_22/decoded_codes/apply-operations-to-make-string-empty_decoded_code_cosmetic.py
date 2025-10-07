class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def countFrequencies(inputStr: str, freqMap: dict) -> None:
            pos = 0
            while pos < len(inputStr):
                currentChar = inputStr[pos]
                if currentChar not in freqMap:
                    freqMap[currentChar] = 1
                else:
                    freqMap[currentChar] += 1
                pos += 1

        frequencies = {}
        countFrequencies(s, frequencies)

        highestFreq = 0
        keyIter = 0
        keyList = list(frequencies.keys())
        while keyIter < len(frequencies):
            currentKey = keyList[keyIter]
            if frequencies[currentKey] > highestFreq:
                highestFreq = frequencies[currentKey]
            keyIter += 1

        chosenChars = set()
        for k in frequencies:
            if frequencies[k] == highestFreq:
                chosenChars.add(k)

        collected = []
        idx = len(s) - 1
        while idx >= 0:
            elem = s[idx]
            if elem in chosenChars:
                collected.append(elem)
                chosenChars.remove(elem)
            idx -= 1

        def reverseConcat(listData: list) -> str:
            acc = ""
            indexVar = len(listData) - 1
            while indexVar >= 0:
                acc += listData[indexVar]
                indexVar -= 1
            return acc

        return reverseConcat(collected)