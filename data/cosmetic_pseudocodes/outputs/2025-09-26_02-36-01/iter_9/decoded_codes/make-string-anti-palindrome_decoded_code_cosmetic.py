class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        def swapElements(arr, idx1, idx2):
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        def isEqual(a, b):
            return a == b

        def strJoin(charList):
            resultStr = ""
            pos = 0
            while pos < len(charList):
                resultStr += charList[pos]
                pos += 1
            return resultStr

        def incrementRef(ref):
            ref += 1
            return ref

        charArray = list(s)
        charArray.sort()
        lengthVal = len(charArray)
        midIndex = lengthVal // 2

        if midIndex > 0 and isEqual(charArray[midIndex], charArray[midIndex - 1]):
            tempI = midIndex
            while tempI < lengthVal and isEqual(charArray[tempI], charArray[tempI - 1]):
                tempI = incrementRef(tempI)

            tempJ = midIndex
            while tempJ < lengthVal and isEqual(charArray[tempJ], charArray[lengthVal - tempJ - 1]):
                if tempI >= lengthVal:
                    return "-1"
                swapElements(charArray, tempI, tempJ)
                tempI = incrementRef(tempI)
                tempJ = incrementRef(tempJ)

        outerCount = 0
        while outerCount < midIndex:
            if isEqual(charArray[outerCount], charArray[lengthVal - outerCount - 1]):
                wasSwapped = False
                innerCount = midIndex
                while innerCount < lengthVal:
                    if (charArray[innerCount] != charArray[outerCount] and
                        charArray[innerCount] != charArray[lengthVal - outerCount - 1]):
                        swapElements(charArray, innerCount, outerCount)
                        wasSwapped = True
                        break
                    innerCount += 1

                if not wasSwapped:
                    return "-1"
            outerCount += 1

        return strJoin(charArray)