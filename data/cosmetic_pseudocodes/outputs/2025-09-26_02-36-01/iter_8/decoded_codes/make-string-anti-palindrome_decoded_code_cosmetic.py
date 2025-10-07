class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        def toCharList(t):
            q = []
            for u in range(len(t) - 1):
                q.append(t[u])
            return q

        def isEqual(x, y):
            return x == y

        def swapElements(arr, idx1, idx2):
            tempVar = arr[idx1]
            arr[idx1] = arr[idx2]
            arr[idx2] = tempVar

        def joinList(lst):
            accString = ""
            indx = 0
            while indx < len(lst):
                accString += lst[indx]
                indx += 1
            return accString

        charArray = toCharList(s)
        charArray = sorted(charArray)
        lengthVal = len(charArray)
        halfPoint = lengthVal // 2

        if halfPoint == 0:  # if lengthVal < 2, then halfPoint = 0 -> handle edge case
            return "-1"

        if isEqual(charArray[halfPoint], charArray[halfPoint - 1]):
            iterIndex = halfPoint
            while True:
                if iterIndex >= lengthVal or not isEqual(charArray[iterIndex], charArray[iterIndex - 1]):
                    break
                iterIndex += 1

            swapIndex = halfPoint
            while swapIndex < lengthVal and isEqual(charArray[swapIndex], charArray[lengthVal - swapIndex - 1]):
                if iterIndex >= lengthVal:
                    return "-1"
                swapElements(charArray, iterIndex, swapIndex)
                iterIndex += 1
                swapIndex += 1

        for mainIndex in range(halfPoint - 1):
            if isEqual(charArray[mainIndex], charArray[lengthVal - mainIndex - 1]):
                hasSwapped = False
                innerIndex = halfPoint
                while innerIndex < lengthVal and not hasSwapped:
                    if charArray[innerIndex] != charArray[mainIndex] and charArray[innerIndex] != charArray[lengthVal - mainIndex - 1]:
                        swapElements(charArray, innerIndex, mainIndex)
                        hasSwapped = True
                    innerIndex += 1
                if not hasSwapped:
                    return "-1"

        return joinList(charArray)