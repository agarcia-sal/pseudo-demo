from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr):
        countMap = defaultdict(int)
        resultList = []

        for s in arr:
            length = len(s)
            for start in range(length):
                for end in range(start + 1, length + 1):
                    substring = s[start:end]
                    countMap[substring] += 1

        for s in arr:
            length = len(s)
            shortest = ""
            for start in range(length):
                for end in range(start + 1, length + 1):
                    substring = s[start:end]
                    if countMap[substring] == 1:
                        if (shortest == "") or (len(substring) < len(shortest)) or (len(substring) == len(shortest) and substring < shortest):
                            shortest = substring
            resultList.append(shortest)

        return resultList