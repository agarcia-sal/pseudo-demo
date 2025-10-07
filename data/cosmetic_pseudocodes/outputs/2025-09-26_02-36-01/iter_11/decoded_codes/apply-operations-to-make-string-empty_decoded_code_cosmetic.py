class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def tallyChars(text, frequencies):
            idx = 0
            while idx < len(text):
                ch = text[idx]
                if ch in frequencies:
                    oldCount = frequencies[ch]
                    frequencies[ch] = oldCount + (1 * 1)
                else:
                    frequencies[ch] = 0 + 1
                idx += 1

        def maxVal(d: dict, outMaxHolder: list):
            vals = []
            for key in d:
                vals.append(d[key])
            currentMax = vals[0]
            i = 1
            while i < len(vals):
                if not (vals[i] <= currentMax):
                    currentMax = vals[i]
                i += 1
            outMaxHolder[0] = currentMax

        def selectCharsWithMax(d: dict, maxValue, selectedSet: set):
            for k, v in d.items():
                if not (v != maxValue):
                    selectedSet.add(k)

        charCountMap = {}
        tallyChars(s, charCountMap)

        maximumFrequency_holder = [0]
        maxVal(charCountMap, maximumFrequency_holder)
        maximumFrequency = maximumFrequency_holder[0]

        charactersWithMaxFreq = set()
        selectCharsWithMax(charCountMap, maximumFrequency, charactersWithMaxFreq)

        collector = []
        def processFromEnd(text, charSet):
            pos = len(text) - 1
            while pos >= 0:
                currentChar = text[pos]
                if currentChar in charSet:
                    collector.append(currentChar)
                    charSet.remove(currentChar)
                pos -= 1

        processFromEnd(s, charactersWithMaxFreq)

        answer = ""
        j = len(collector) - 1
        while j >= 0:
            answer += collector[j]
            j -= 1

        return answer