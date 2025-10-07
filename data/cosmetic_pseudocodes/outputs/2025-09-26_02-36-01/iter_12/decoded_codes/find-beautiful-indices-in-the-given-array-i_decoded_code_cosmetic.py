class Solution:
    def beautifulIndices(self, s, a, b, k):
        def findAllOccurrences(text, pattern):
            resultIndices = []
            textLength = len(text)
            patternLength = len(pattern)
            pos = 0

            def subStrEqual(t, startIdx, p):
                endIdx = startIdx + len(p) - 1
                idx1 = startIdx
                idx2 = 0
                while idx2 < len(p):
                    if t[idx1] != p[idx2]:
                        return False
                    idx1 += 1
                    idx2 += 1
                return True

            while True:
                if pos >= textLength - patternLength + 1:
                    break
                if subStrEqual(text, pos, pattern):
                    resultIndices.append(pos)
                pos += 1
            return resultIndices

        listA = findAllOccurrences(s, a)
        listB = findAllOccurrences(s, b)

        def absDiff(x, y):
            if x >= y:
                return x - y
            else:
                return y - x

        def checkProximity(list1, list2, maxDist):
            res = []
            iIdx = 0
            while iIdx < len(list1):
                jIdx = 0
                added = False
                while jIdx < len(list2) and not added:
                    if absDiff(list1[iIdx], list2[jIdx]) <= maxDist:
                        res.append(list1[iIdx])
                        added = True
                    jIdx += 1
                iIdx += 1
            return res

        return checkProximity(listA, listB, k)