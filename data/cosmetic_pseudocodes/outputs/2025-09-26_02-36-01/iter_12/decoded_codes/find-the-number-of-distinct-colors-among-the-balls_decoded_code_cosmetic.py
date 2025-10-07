class Solution:
    def queryResults(self, limit, queries):
        def addToSet(s, e):
            if not containsInSet(s, e):
                insertIntoSet(s, e)

        def containsInSet(s, e):
            for item in s:
                if item == e:
                    return True
            return False

        def insertIntoSet(s, e):
            s.append(e)

        def removeFromSet(s, e):
            idx = 0
            found = False
            while idx < len(s) and not found:
                if s[idx] == e:
                    found = True
                else:
                    idx += 1
            if found:
                for j in range(idx, len(s) - 1):
                    s[j] = s[j + 1]
                s.pop()

        def containsKey(d, key):
            for k in d:
                if k == key:
                    return True
            return False

        freqById = dict()
        distinctColors = []
        output = []
        qIdx = 0

        while qIdx < limit:
            queryQ = queries[qIdx]
            keyVal = queryQ[0]
            newCol = queryQ[1]

            if containsKey(freqById, keyVal):
                prevCol = freqById[keyVal]
                if containsInSet(distinctColors, prevCol):
                    removeFromSet(distinctColors, prevCol)

            freqById[keyVal] = newCol
            addToSet(distinctColors, newCol)

            output.append(len(distinctColors))
            qIdx += 1

        return output