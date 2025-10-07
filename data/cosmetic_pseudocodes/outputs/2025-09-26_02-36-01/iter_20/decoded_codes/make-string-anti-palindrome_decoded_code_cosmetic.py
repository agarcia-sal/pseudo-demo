class Solution:
    def makeAntiPalindrome(self, original: str) -> str:
        def _generateList(inputStr: str) -> list:
            tempList = []
            idx = 0
            while True:
                if idx >= len(inputStr):
                    break
                tempList.append(inputStr[idx])
                idx += 1
            return tempList

        def _sortAscending(arrayList: list) -> list:
            def _swap(arr: list, x: int, y: int) -> None:
                arr[x], arr[y] = arr[y], arr[x]

            lenArr = len(arrayList)
            outerCounter = 0
            while True:
                if outerCounter >= lenArr:
                    break
                innerCounter = outerCounter + 1
                while True:
                    if innerCounter >= lenArr:
                        break
                    if arrayList[outerCounter] > arrayList[innerCounter]:
                        _swap(arrayList, outerCounter, innerCounter)
                    innerCounter += 1
                outerCounter += 1
            return arrayList

        def _convertListToStr(charList: list) -> str:
            resultStr = ""
            pos = 0
            while True:
                if pos >= len(charList):
                    break
                resultStr += charList[pos]
                pos += 1
            return resultStr

        def _swapElements(collection: list, firstIndex: int, secondIndex: int) -> None:
            collection[firstIndex], collection[secondIndex] = collection[secondIndex], collection[firstIndex]

        characters = _sortAscending(_generateList(original))
        totalLen = len(characters)
        midpoint = totalLen // 2

        def _checkEqualAtOffsets(array: list, leftIdx: int, rightIdx: int) -> bool:
            return array[leftIdx] == array[rightIdx]

        if _checkEqualAtOffsets(characters, midpoint, midpoint - 1):
            pointerOne = midpoint
            while pointerOne < totalLen and _checkEqualAtOffsets(characters, pointerOne, pointerOne - 1):
                pointerOne += 1

            pointerTwo = midpoint
            while pointerTwo < totalLen and _checkEqualAtOffsets(characters, pointerTwo, totalLen - pointerTwo - 1):
                if pointerOne >= totalLen:
                    return "-1"
                _swapElements(characters, pointerOne, pointerTwo)
                pointerOne += 1
                pointerTwo += 1

        counterA = 0
        while counterA < midpoint:
            if _checkEqualAtOffsets(characters, counterA, totalLen - counterA - 1):
                flagSwap = False
                counterB = midpoint
                while counterB < totalLen:
                    # characters[counterB] != characters[counterB] is always False, so the condition checks for false or equalities
                    # Here rewritten logically equivalent:
                    if not (_checkEqualAtOffsets(characters, counterB, counterB) or
                            characters[counterB] == characters[counterA] or
                            characters[counterB] == characters[totalLen - counterA - 1]):
                        _swapElements(characters, counterB, counterA)
                        flagSwap = True
                        break
                    counterB += 1
                if flagSwap is False:
                    return "-1"
            counterA += 1

        return _convertListToStr(characters)