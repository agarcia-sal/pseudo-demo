class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def pairs():
            collection = ['0', '1', '2', '3', '4']
            result = []
            idx1 = 0
            length = len(collection)
            while idx1 < length:
                idx2 = 0
                while idx2 < length:
                    if collection[idx1] != collection[idx2]:
                        result.append((collection[idx1], collection[idx2]))
                    idx2 += 1
                idx1 += 1
            return result

        def minDefaultDict(defaultValue):
            d = {}

            def getKey(key):
                if key in d:
                    return d[key]
                else:
                    d[key] = defaultValue
                    return d[key]

            def setKey(key, val):
                d[key] = val

            return getKey, setKey

        maximumDifference = -(1 << 30)
        pairsList = pairs()
        length_s = len(s)

        for charA, charB in pairsList:
            getMinDiff, setMinDiff = minDefaultDict(1 << 30)
            prefixCountA = [0]
            prefixCountB = [0]
            leftIdx = 0

            # processIndex defined as inner function to capture variables by closure
            def processIndex(currentIndex, currCharA, currCharB):
                nonlocal leftIdx, maximumDifference

                incrementA = 1 if currCharA == charA else 0
                incrementB = 1 if currCharB == charB else 0

                prefixCountA.append(prefixCountA[-1] + incrementA)
                prefixCountB.append(prefixCountB[-1] + incrementB)

                # slide leftIdx forward maintaining window and conditions
                while (
                    (currentIndex + 1 - leftIdx) >= k
                    and prefixCountA[leftIdx] < prefixCountA[-1]
                    and prefixCountB[leftIdx] < prefixCountB[-1]
                ):
                    keyTuple = (prefixCountA[leftIdx] % 2, prefixCountB[leftIdx] % 2)
                    pairMinDiff = getMinDiff(keyTuple)
                    currentDiff = prefixCountA[leftIdx] - prefixCountB[leftIdx]
                    if currentDiff < pairMinDiff:
                        setMinDiff(keyTuple, currentDiff)
                    leftIdx += 1

                lastIndex = len(prefixCountA) - 1
                modA = prefixCountA[lastIndex] % 2
                modB = prefixCountB[lastIndex] % 2
                lookupKey = ((1 - modA), modB)

                candidateDiff = prefixCountA[lastIndex] - prefixCountB[lastIndex] - getMinDiff(lookupKey)
                if candidateDiff > maximumDifference:
                    maximumDifference = candidateDiff

            pos = 0
            while pos < length_s:
                processIndex(pos, s[pos], s[pos])
                pos += 1

        return maximumDifference