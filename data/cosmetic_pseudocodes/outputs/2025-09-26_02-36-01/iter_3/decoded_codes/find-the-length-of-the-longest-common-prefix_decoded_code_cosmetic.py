class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        collectedPrefixes1 = set()
        idx1 = 0
        while idx1 < len(arr1):
            currentNum1 = arr1[idx1]
            currentStr1 = str(currentNum1)
            length1 = len(currentStr1)
            pos1 = 1
            while pos1 <= length1:
                subStr1 = currentStr1[:pos1]
                collectedPrefixes1.add(subStr1)
                pos1 += 1
            idx1 += 1

        collectedPrefixes2 = set()
        idx2 = 0
        while idx2 < len(arr2):
            currentNum2 = arr2[idx2]
            currentStr2 = str(currentNum2)
            length2 = len(currentStr2)
            pos2 = 1
            while pos2 <= length2:
                subStr2 = currentStr2[:pos2]
                collectedPrefixes2.add(subStr2)
                pos2 += 1
            idx2 += 1

        maxCommonLen = 0
        for prefix in collectedPrefixes1:
            if prefix in collectedPrefixes2:
                lenPrefix = len(prefix)
                if lenPrefix > maxCommonLen:
                    maxCommonLen = lenPrefix

        return maxCommonLen