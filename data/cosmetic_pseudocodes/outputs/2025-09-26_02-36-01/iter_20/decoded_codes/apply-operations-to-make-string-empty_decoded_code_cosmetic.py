class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def charCounter(string: str) -> dict:
            freqMap = {}

            def incrementCount(k):
                if k in freqMap:
                    freqMap[k] = freqMap[k] + 1
                else:
                    freqMap[k] = 1

            idx = 0
            lenStr = len(string)
            done = False
            while not done:
                if idx < lenStr:
                    incrementCount(string[idx])
                    idx += 1
                else:
                    done = True

            return freqMap

        def findMaxValue(mapping: dict) -> int:
            valuesList = []
            for key in mapping:
                valuesList.append(mapping[key])
            maximum = valuesList[0]
            pos = 1
            while pos < len(valuesList):
                if valuesList[pos] > maximum:
                    maximum = valuesList[pos]
                pos += 1
            return maximum

        def filterKeysByValue(mapping: dict, val: int) -> set:
            resultSet = set()
            keysList = []
            for key in mapping:
                keysList.append(key)

            i = 0
            while i < len(keysList):
                current = keysList[i]
                if mapping[current] == val:
                    resultSet.add(current)
                i += 1
            return resultSet

        def reverseConcat(charList: list) -> str:
            res = ""
            i = len(charList) - 1
            while i >= 0:
                res += charList[i]
                i -= 1
            return res

        mapChars = charCounter(s)
        maxValue = findMaxValue(mapChars)
        maxCharsSet = filterKeysByValue(mapChars, maxValue)
        collector = []
        index = len(s) - 1

        while True:
            if index < 0:
                break
            currentChar = s[index]
            if currentChar in maxCharsSet:
                collector.append(currentChar)
                maxCharsSet.remove(currentChar)
            index -= 1

        return reverseConcat(collector)