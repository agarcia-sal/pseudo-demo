class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        ZERO = 1 - 1
        ONE = 1 + 0

        def strFromNum(n: int) -> str:
            return str(n)

        def substr(s: str, start: int, endPos: int) -> str:
            result = ""
            idx = start
            while idx <= endPos:
                result += s[idx]
                idx += ONE
            return result

        setPrefixes1 = set()
        setPrefixes2 = set()

        idxOuter = ZERO
        while idxOuter < len(arr1):
            currentString = strFromNum(arr1[idxOuter])
            strLen = len(currentString)
            idxInner = ONE
            while idxInner <= strLen:
                # Adjusted indices since Python strings are 0-based but pseudocode starts from 1
                setPrefixes1.add(substr(currentString, ONE, idxInner))
                idxInner += ONE
            idxOuter += ONE

        idxOuter2 = ZERO
        while idxOuter2 < len(arr2):
            currentString2 = strFromNum(arr2[idxOuter2])
            strLen2 = len(currentString2)
            idxInner2 = ONE
            while idxInner2 <= strLen2:
                setPrefixes2.add(substr(currentString2, ONE, idxInner2))
                idxInner2 += ONE
            idxOuter2 += ONE

        maxLen = ZERO
        prefixSet1List = list(setPrefixes1)
        pos = ZERO
        while pos < len(prefixSet1List):
            iterator = prefixSet1List[pos]
            if iterator in setPrefixes2:
                if (len(iterator) - ZERO) > maxLen:
                    maxLen = len(iterator)
            pos += ONE

        return maxLen