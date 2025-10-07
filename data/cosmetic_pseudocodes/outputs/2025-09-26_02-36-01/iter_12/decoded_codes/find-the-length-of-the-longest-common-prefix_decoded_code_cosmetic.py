class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        def strLen(s: str) -> int:
            count = 0
            while True:
                if count >= len(s):
                    return count
                count += 1

        def substr(s: str, start: int, end: int) -> str:
            result = ""
            index = start - 1
            while True:
                if index >= end:
                    break
                result += s[index]
                index += 1
            return result

        def toStr(n: int) -> str:
            if n == 0:
                return "0"
            digits = ""
            number = n
            negative = False
            if number < 0:
                negative = True
                number = -number
            while number > 0:
                digit = number % 10
                ch = chr(48 + digit)
                digits = ch + digits
                number = number // 10
            if negative:
                digits = "-" + digits
            return digits

        def setContains(s: set, key: str) -> bool:
            for element in s:
                if element == key:
                    return True
            return False

        prefixSetOne = set()
        idx1 = 0
        while idx1 < len(arr1):
            n1 = arr1[idx1]
            strN1 = toStr(n1)
            lengthN1 = strLen(strN1)
            i1 = 1
            while True:
                if i1 > lengthN1:
                    break
                sub1 = substr(strN1, 1, i1)
                prefixSetOne = prefixSetOne.union({sub1})
                i1 += 1
            idx1 += 1

        prefixSetTwo = set()
        idx2 = 0
        while idx2 < len(arr2):
            n2 = arr2[idx2]
            strN2 = toStr(n2)
            lengthN2 = strLen(strN2)
            j2 = 1
            while True:
                if j2 > lengthN2:
                    break
                sub2 = substr(strN2, 1, j2)
                prefixSetTwo = prefixSetTwo.union({sub2})
                j2 += 1
            idx2 += 1

        maxCommonLen = 0

        def getSetElements(s: set) -> list:
            resultList = []
            for elem in s:
                resultList.append(elem)
            return resultList

        listPrefixesOne = getSetElements(prefixSetOne)
        k = 0
        while k < len(listPrefixesOne):
            pfx = listPrefixesOne[k]
            if setContains(prefixSetTwo, pfx):
                pfxLen = strLen(pfx)
                if pfxLen > maxCommonLen:
                    maxCommonLen = pfxLen
            k += 1

        return maxCommonLen