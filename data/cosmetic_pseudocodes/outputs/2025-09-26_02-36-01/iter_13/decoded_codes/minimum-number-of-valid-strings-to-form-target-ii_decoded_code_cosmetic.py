from math import inf

class Solution:
    def minValidStrings(self, words, target):
        def containsPrefix(setCollection, query):
            for idx in range(1, len(query) + 1):
                if query[:idx] in setCollection:
                    return True
            return False

        def getMin(a, b):
            return a if a <= b else b

        def buildPrefixes(srcWords, prefixSet):
            def insertPrefixes(word, count):
                if count > len(word):
                    return
                prefixSet.add(word[:count])
                insertPrefixes(word, count + 1)

            for w in srcWords:
                insertPrefixes(w, 1)

        prefixes = set()
        buildPrefixes(words, prefixes)

        lengthTarget = len(target)
        dpList = [inf] * (lengthTarget + 1)
        dpList[0] = 0

        def updateDP(pos):
            if pos > lengthTarget:
                return

            def innerCheck(begin):
                if begin > pos:
                    return
                subStr = target[begin - 1:pos]
                if subStr in prefixes:
                    dpList[pos] = getMin(dpList[pos], dpList[begin - 1] + 1)
                innerCheck(begin + 1)

            innerCheck(1)
            updateDP(pos + 1)

        updateDP(1)

        return dpList[lengthTarget] if dpList[lengthTarget] < inf else -1