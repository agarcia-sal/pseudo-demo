class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixesSetOne = set()
        for num in arr1:
            stringNum = str(num)
            for indexVar in range(1, len(stringNum) + 1):
                tempPrefix = stringNum[:indexVar]
                prefixesSetOne.add(tempPrefix)

        prefixesSetTwo = set()
        for num in arr2:
            stringNum = str(num)
            for indexVar in range(1, len(stringNum) + 1):
                tempPrefix = stringNum[:indexVar]
                prefixesSetTwo.add(tempPrefix)

        maxCommonLength = 0
        for prefixElem in prefixesSetOne:
            if prefixElem in prefixesSetTwo and len(prefixElem) > maxCommonLength:
                maxCommonLength = len(prefixElem)

        return maxCommonLength