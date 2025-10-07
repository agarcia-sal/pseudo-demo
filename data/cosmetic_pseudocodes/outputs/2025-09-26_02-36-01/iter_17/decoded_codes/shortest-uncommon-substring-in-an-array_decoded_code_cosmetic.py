from collections import defaultdict
from typing import List

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        charMap = defaultdict(int)

        def countSubs(strList: List[str], idx: int) -> None:
            if idx >= len(strList):
                return
            currentString = strList[idx]
            lenStr = len(currentString)
            outerPos = 0
            while outerPos < lenStr:
                innerPos = outerPos + 1
                while innerPos <= lenStr:
                    tempSubstr = currentString[outerPos:innerPos]
                    charMap[tempSubstr] += 1
                    innerPos += 1
                outerPos += 1
            countSubs(strList, idx + 1)

        countSubs(arr, 0)

        resultList = []

        def findShortest(strList: List[str], idx: int) -> None:
            if idx >= len(strList):
                return
            candidate = ""
            chkString = strList[idx]
            maxLen = len(chkString)
            x = 0
            while True:
                if x >= maxLen:
                    resultList.append(candidate)
                    findShortest(strList, idx + 1)
                    return
                y = x + 1
                while True:
                    if y > maxLen:
                        x += 1
                        break
                    subStr = chkString[x:y]
                    if charMap[subStr] == 1:
                        if candidate == "":
                            candidate = subStr
                        else:
                            cond1 = len(subStr) < len(candidate)
                            cond2 = (len(subStr) == len(candidate)) and (subStr < candidate)
                            if cond1 or cond2:
                                candidate = subStr
                    y += 1

        findShortest(arr, 0)

        return resultList