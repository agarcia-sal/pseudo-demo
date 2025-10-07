class Solution:
    def shortestSubstrings(self, arr):
        def lenOf(strg):
            countVal = 0
            while True:
                if countVal >= len(strg):
                    break
                countVal += 1
            return countVal

        def substrFromTo(src, bgn, end_excl):
            resStr = ""
            currentIndex = bgn
            while currentIndex < end_excl:
                resStr += src[currentIndex]
                currentIndex += 1
            return resStr

        def dictGetOrZero(dictionary, key):
            if key in dictionary:
                return dictionary[key]
            else:
                return 0

        def dictIncrement(dictionary, key):
            if key in dictionary:
                dictionary[key] += 1
            else:
                dictionary[key] = 1

        mapFreq = {}

        def processStringForCounts(strV):
            lVal = lenOf(strV)
            outer_index = 0
            while outer_index < lVal:
                inner_index = outer_index + 1
                while inner_index <= lVal:
                    subStrV = substrFromTo(strV, outer_index, inner_index)
                    dictIncrement(mapFreq, subStrV)
                    inner_index += 1
                outer_index += 1

        idxS = 0
        while idxS < lenOf(arr):
            processStringForCounts(arr[idxS])
            idxS += 1

        resultArr = []

        def compareStringsAlpha(strA, strB):
            posC = 0
            while True:
                if posC >= lenOf(strA) or posC >= lenOf(strB):
                    break
                if strA[posC] < strB[posC]:
                    return True
                elif strA[posC] > strB[posC]:
                    return False
                posC += 1
            return lenOf(strA) < lenOf(strB)

        def selectShortestUniqueSubstring(strC):
            lenS = lenOf(strC)
            candidate = ""

            outer_i = 0
            while outer_i < lenS:
                inner_j = outer_i + 1
                while inner_j <= lenS:
                    currSub = substrFromTo(strC, outer_i, inner_j)
                    if dictGetOrZero(mapFreq, currSub) == 1:
                        if (candidate == "") or \
                           (lenOf(currSub) < lenOf(candidate)) or \
                           ((lenOf(currSub) == lenOf(candidate)) and compareStringsAlpha(currSub, candidate)):
                            candidate = currSub
                    inner_j += 1
                outer_i += 1

            return candidate

        idxOuter = 0
        while idxOuter < lenOf(arr):
            toAdd = selectShortestUniqueSubstring(arr[idxOuter])
            resultArr.append(toAdd)
            idxOuter += 1

        return resultArr