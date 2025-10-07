class Solution:
    def clearStars(self, s: str) -> str:
        tempList = []
        idx_1 = 0

        while idx_1 < len(s):
            nxtChar = s[idx_1]
            if nxtChar == '*':
                if tempList:
                    tempList.pop()
            else:
                tempList.append(nxtChar)
            idx_1 += 1

        tempStr = ""
        idx_2 = 0

        while True:
            if idx_2 >= len(tempList):
                break
            tempStr += tempList[idx_2]
            idx_2 += 1

        return tempStr