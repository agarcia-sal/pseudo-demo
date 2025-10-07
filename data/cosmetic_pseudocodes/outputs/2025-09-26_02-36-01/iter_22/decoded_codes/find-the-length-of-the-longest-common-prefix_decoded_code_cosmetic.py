class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        setA = set()

        def AddAllPrefixes(sequence: list[int]) -> None:
            for element in sequence:
                elementStr = str(element)
                for prefixLen in range(1, len(elementStr) + 1):
                    setA.add(elementStr[:prefixLen])

        AddAllPrefixes(arr1)

        setB = set()

        def AddAllPrefixesToB(sequence: list[int]) -> None:
            for element in sequence:
                elemStr = str(element)
                for p in range(1, len(elemStr) + 1):
                    setB.add(elemStr[:p])

        AddAllPrefixesToB(arr2)

        maxLen = 0
        for prefixIter in setA:
            if prefixIter in setB:
                lengthPrefix = len(prefixIter)
                if lengthPrefix > maxLen:
                    maxLen = lengthPrefix

        return maxLen