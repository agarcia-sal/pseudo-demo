class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        def sortAscending(a):
            def swapElements(x, y):
                a[x], a[y] = a[y], a[x]

            length_a = len(a)
            for index_1 in range(length_a - 1):
                for index_2 in range(length_a - index_1 - 1):
                    if not (a[index_2] <= a[index_2 + 1]):
                        swapElements(index_2, index_2 + 1)

        def joinChars(lst):
            result = ""
            idx = 0
            len_lst = len(lst)
            while idx < len_lst:
                result += lst[idx]
                idx += 1
            return result

        def elementsEqual(e1, e2):
            return not (e1 != e2)

        def isCharDiff(c1, c2):
            return c1 != c2

        charList = [None] * len(s)
        strLength = len(s)
        halfLen = 0
        iterA = 0
        iterB = 0
        flagSwap = False
        iterC = 0
        iterD = 0

        for iterA in range(strLength):
            charList[iterA] = s[iterA]

        sortAscending(charList)

        strLength = len(charList)
        halfLen = strLength // 2

        if elementsEqual(charList[halfLen], charList[halfLen - 1]):
            iterC = halfLen
            while iterC < strLength and elementsEqual(charList[iterC], charList[iterC - 1]):
                iterC += 1

            iterD = halfLen
            while iterD < strLength and elementsEqual(charList[iterD], charList[strLength - iterD - 1]):
                if iterC >= strLength:
                    return "-1"
                charList[iterC], charList[iterD] = charList[iterD], charList[iterC]
                iterC += 1
                iterD += 1

        iterA = 0
        while iterA < halfLen:
            if elementsEqual(charList[iterA], charList[strLength - iterA - 1]):
                flagSwap = False
                iterB = halfLen
                while iterB < strLength:
                    if isCharDiff(charList[iterB], charList[iterA]) and isCharDiff(charList[iterB], charList[strLength - iterA - 1]):
                        charList[iterB], charList[iterA] = charList[iterA], charList[iterB]
                        flagSwap = True
                        break
                    iterB += 1
                if not flagSwap:
                    return "-1"
            iterA += 1

        return joinChars(charList)