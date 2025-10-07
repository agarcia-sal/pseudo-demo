class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        def freqCounter(string: str) -> dict:
            freqMap = {}
            idxCounter = 0
            while idxCounter < len(string):
                symb = string[idxCounter]
                if symb in freqMap:
                    freqMap[symb] += 1
                else:
                    freqMap[symb] = 1
                idxCounter += 1
            return freqMap

        def determineMaxVal(m: dict) -> int:
            vals = [m[k] for k in m.keys()]
            if len(vals) == 0:
                return 0
            largest = vals[0]
            i = 1
            while i < len(vals):
                if vals[i] > largest:
                    largest = vals[i]
                i += 1
            return largest

        def collectMaxFreqChars(m: dict, target: int) -> set:
            container = set()
            for k in m.keys():
                if m[k] == target:
                    container.add(k)
            return container

        def lastToFirstConcat(lst: list) -> str:
            resStr = ""
            i = len(lst) - 1
            while i >= 0:
                resStr += lst[i]
                i -= 1
            return resStr

        charTally = freqCounter(s)
        maximumCount = determineMaxVal(charTally)
        freqMaxChars = collectMaxFreqChars(charTally, maximumCount)
        collected = []

        def descendIndex(j: int):
            if j < 0:
                return
            curChar = s[j]
            if curChar in freqMaxChars:
                collected.append(curChar)
                freqMaxChars.remove(curChar)
            descendIndex(j - 1)

        descendIndex(len(s) - 1)
        return lastToFirstConcat(collected)