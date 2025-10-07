class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        tempList1 = []
        pos1 = 0
        s_len = len(s)
        a_len = len(a)
        b_len = len(b)

        while pos1 <= s_len - a_len:
            subStr1 = s[pos1:pos1 + a_len]
            if subStr1 == a:
                tempList1.append(pos1)
            pos1 += 1

        tempList2 = []
        pos2 = 0
        while pos2 <= s_len - b_len:
            accStr = s[pos2:pos2 + b_len]
            if accStr == b:
                tempList2.append(pos2)
            pos2 += 1

        resultList = []
        idxA = 0
        idxB = 0
        while idxA < len(tempList1) and idxB < len(tempList2):
            diffVal = abs(tempList1[idxA] - tempList2[idxB])
            if diffVal <= k:
                resultList.append(tempList1[idxA])
                idxA += 1
            else:
                if tempList1[idxA] < tempList2[idxB]:
                    idxA += 1
                else:
                    idxB += 1

        return resultList