class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        def swapElements(arr, x, y):
            arr[x], arr[y] = arr[y], arr[x]

        def recursiveCheck(pIndex, limitIndex, offset, collection):
            if pIndex < limitIndex and collection[pIndex] == collection[pIndex - offset]:
                return recursiveCheck(pIndex + 1, limitIndex, offset, collection)
            return pIndex

        def recursiveSecondaryScan(startIndex, endIndex, col):
            if startIndex < endIndex and col[startIndex] == col[endIndex - startIndex - 1]:
                return recursiveSecondaryScan(startIndex + 1, endIndex, col)
            return startIndex

        def findSuitableSwap(xIndex, upperBound, candidates, target1, target2):
            if xIndex > upperBound:
                return False, xIndex
            if candidates[xIndex] != target1 and candidates[xIndex] != target2:
                return True, xIndex
            return findSuitableSwap(xIndex + 1, upperBound, candidates, target1, target2)

        characterList = [ch for ch in s]

        def insertionSort(arr):
            def innerSort(idx, length, arrRef):
                if idx >= length:
                    return
                keyVal = arrRef[idx]
                pos = idx - 1
                while pos >= 0 and arrRef[pos] > keyVal:
                    arrRef[pos + 1] = arrRef[pos]
                    pos -= 1
                arrRef[pos + 1] = keyVal
                innerSort(idx + 1, length, arrRef)
            innerSort(1, len(arr), arr)

        insertionSort(characterList)

        lenChars = len(characterList)
        midPoint = (lenChars - (lenChars % 2)) // 2

        if lenChars == 0:
            return ""

        if midPoint == 0:
            # With empty or single char string, palindrome check differs
            # If single char, can't form anti-palindrome
            # Return original string if no palindromic halves exist
            return s if lenChars == 1 else "-1"

        if characterList[midPoint] == characterList[midPoint - 1]:
            firstCounter = recursiveCheck(midPoint, lenChars, 1, characterList)
            secondCounter = midPoint
            while secondCounter < lenChars and characterList[secondCounter] == characterList[lenChars - secondCounter - 1]:
                if firstCounter >= lenChars:
                    return "-1"
                swapElements(characterList, firstCounter, secondCounter)
                firstCounter += 1
                secondCounter += 1

        def traverseIndex(currentIndex, limitIndex, arrChars):
            if currentIndex >= limitIndex:
                return True
            if arrChars[currentIndex] == arrChars[lenChars - currentIndex - 1]:
                swappedFlag = False

                def innerSwap(kIndex, maxIndex):
                    nonlocal swappedFlag
                    if kIndex > maxIndex or swappedFlag:
                        return
                    if arrChars[kIndex] != arrChars[currentIndex] and arrChars[kIndex] != arrChars[lenChars - currentIndex -1]:
                        swapElements(arrChars, kIndex, currentIndex)
                        swappedFlag = True
                        return
                    innerSwap(kIndex + 1, maxIndex)

                innerSwap(midPoint, lenChars - 1)
                if not swappedFlag:
                    return False
            return traverseIndex(currentIndex + 1, limitIndex, arrChars)

        traversalResult = traverseIndex(0, midPoint, characterList)
        if traversalResult is False:
            return "-1"

        return "".join(characterList)