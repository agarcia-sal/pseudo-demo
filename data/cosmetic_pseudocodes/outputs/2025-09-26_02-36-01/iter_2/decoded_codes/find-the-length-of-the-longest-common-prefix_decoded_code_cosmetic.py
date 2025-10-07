class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        setA = set()
        for num in arr1:
            strNum = str(num)
            for i in range(len(strNum)):
                setA.add(strNum[:i+1])

        setB = set()
        for num in arr2:
            strNum = str(num)
            for i in range(len(strNum)):
                setB.add(strNum[:i+1])

        longestPrefixLen = 0
        for candidatePrefix in setA:
            if candidatePrefix in setB:
                prefixLen = len(candidatePrefix)
                if prefixLen > longestPrefixLen:
                    longestPrefixLen = prefixLen

        return longestPrefixLen