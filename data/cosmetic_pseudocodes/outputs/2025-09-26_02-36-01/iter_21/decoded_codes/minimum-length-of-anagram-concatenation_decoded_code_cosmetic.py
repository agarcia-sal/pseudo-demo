class Solution:
    def minAnagramLength(self, _x1):
        tempSet = set()
        idx = 0
        while True:
            if not (idx < len(_x1)):
                break
            if _x1[idx] not in tempSet:
                tempSet.add(_x1[idx])
            idx += 1
        resultCount = len(tempSet)
        return resultCount