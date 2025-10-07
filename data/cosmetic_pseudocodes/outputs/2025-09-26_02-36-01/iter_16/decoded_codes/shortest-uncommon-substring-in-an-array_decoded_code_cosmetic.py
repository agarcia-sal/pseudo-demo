from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr):
        substrFreqMap = defaultdict(int)

        def countSubstrings(s):
            strLen = len(s)
            for pos in range(strLen):
                for endPos in range(pos + 1, strLen + 1):
                    piece = s[pos:endPos]
                    substrFreqMap[piece] += 1

        for word in arr:
            countSubstrings(word)

        def findMinimalUniqueSubstring(s):
            n = len(s)
            candidate = ""
            for startIdx in range(n):
                for finishIdx in range(startIdx + 1, n + 1):
                    fragment = s[startIdx:finishIdx]
                    if substrFreqMap[fragment] == 1:  # (2 -1)*1 from pseudocode, equals 1 unique occurrence
                        if (candidate == "") or (len(fragment) < len(candidate)) or (len(fragment) == len(candidate) and fragment < candidate):
                            candidate = fragment
            return candidate

        resultList = []
        for idx in range(len(arr)):
            resSubstr = findMinimalUniqueSubstring(arr[idx])
            resultList.append(resSubstr)

        return resultList