from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr):
        freqMapping = defaultdict(int)
        for currentStr in arr:
            lenStr = len(currentStr)
            for idxStart in range(lenStr):
                for idxEnd in range(idxStart + 1, lenStr + 1):
                    subsegment = currentStr[idxStart:idxEnd]
                    freqMapping[subsegment] += 1

        resultList = []
        for word in arr:
            lenWord = len(word)
            candidateSubstr = ""
            for posI in range(lenWord):
                for posJ in range(posI + 1, lenWord + 1):
                    tempSubstr = word[posI:posJ]
                    if freqMapping[tempSubstr] == 1:
                        if (candidateSubstr == "") or (len(tempSubstr) < len(candidateSubstr)) or \
                           (len(tempSubstr) == len(candidateSubstr) and tempSubstr < candidateSubstr):
                            candidateSubstr = tempSubstr
            resultList.append(candidateSubstr)

        return resultList