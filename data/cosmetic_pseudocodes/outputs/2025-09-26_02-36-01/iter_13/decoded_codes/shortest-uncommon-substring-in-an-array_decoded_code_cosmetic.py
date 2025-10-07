class Solution:
    def shortestSubstrings(self, arr):
        def dictWithDefaultZero():
            mapVar = {}

            def getValue(key):
                return mapVar.get(key, 0)

            def setValue(key, val):
                mapVar[key] = val

            return getValue, setValue

        getCount, setCount = dictWithDefaultZero()

        def incrCount(key):
            currVal = getCount(key)
            setCount(key, currVal + 1)

        def substring(s, startIndex, endIndex):
            result = []
            def recurCopy(pos):
                if pos >= endIndex:
                    return
                result.append(s[pos])
                recurCopy(pos + 1)
            recurCopy(startIndex)
            return ''.join(result)

        def generateSubstrings(s, actionFunc):
            strLen = len(s)

            def outerLoop(i):
                if i >= strLen:
                    return
                def innerLoop(j):
                    if j > strLen:
                        return
                    sub = substring(s, i, j)
                    actionFunc(sub)
                    innerLoop(j + 1)
                innerLoop(i + 1)
                outerLoop(i + 1)
            outerLoop(0)

        def addCountingToDict(subStr):
            incrCount(subStr)

        def minStringCompare(a, b):
            if a == "":
                return b
            elif b == "":
                return a
            if len(a) < len(b):
                return a
            elif len(a) > len(b):
                return b
            else:
                def lessThan(str1, str2, idx):
                    if idx >= len(str1):
                        return False
                    if str1[idx] < str2[idx]:
                        return True
                    elif str1[idx] > str2[idx]:
                        return False
                    else:
                        return lessThan(str1, str2, idx + 1)
                if lessThan(a, b, 0):
                    return a
                else:
                    return b

        def getCountSafe(s):
            return getCount(s)

        def findShortestUnique(s):
            shortest = ""
            strLen = len(s)

            def outer(i):
                nonlocal shortest
                if i >= strLen:
                    return
                def inner(j):
                    nonlocal shortest
                    if j > strLen:
                        return
                    candidate = substring(s, i, j)
                    if getCountSafe(candidate) == 1:
                        shortest = minStringCompare(shortest, candidate)
                    inner(j + 1)
                inner(i + 1)
                outer(i + 1)
            outer(0)
            return shortest

        def processArr(arr):
            idx = 0
            def loop():
                nonlocal idx
                if idx >= len(arr):
                    return
                elem = arr[idx]
                generateSubstrings(elem, addCountingToDict)
                idx += 1
                loop()
            loop()

        def generateAnswer(arr):
            outIdx = 0
            answers = []
            def recAns():
                nonlocal outIdx, answers
                if outIdx >= len(arr):
                    return
                currStr = arr[outIdx]
                uniqueSub = findShortestUnique(currStr)
                answers.append(uniqueSub)
                outIdx += 1
                recAns()
            recAns()
            return answers

        processArr(arr)
        return generateAnswer(arr)