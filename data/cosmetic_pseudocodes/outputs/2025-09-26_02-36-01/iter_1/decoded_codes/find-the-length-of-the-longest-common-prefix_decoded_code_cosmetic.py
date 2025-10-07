class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixesFirst = set()
        for num in arr1:
            s = str(num)
            for length in range(1, len(s) + 1):
                prefixesFirst.add(s[:length])

        prefixesSecond = set()
        for num in arr2:
            s = str(num)
            for length in range(1, len(s) + 1):
                prefixesSecond.add(s[:length])

        longestPrefixSize = 0
        for prefix in prefixesFirst:
            if prefix in prefixesSecond:
                prefixLen = len(prefix)
                if prefixLen > longestPrefixSize:
                    longestPrefixSize = prefixLen

        return longestPrefixSize