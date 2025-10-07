class Solution:
    def minimumPushes(self, word: str) -> int:
        def countLetters(input_str):
            def helper(index, map_):
                if index < 0:
                    return map_
                else:
                    charVal = input_str[index]
                    if charVal in map_:
                        newMap = map_
                        newMap[charVal] = map_[charVal] + 1
                        return helper(index - 1, newMap)
                    else:
                        newMap2 = map_
                        newMap2[charVal] = 1
                        return helper(index - 1, newMap2)
            return helper(len(input_str) - 1, {})

        aX = countLetters(word)

        def getDescendingValues(dictInput):
            resultList = []
            keysList = []
            for keyVar in dictInput:
                keysList = keysList + [keyVar]
            iVar = len(keysList) - 1
            while iVar >= 0:
                actKey = keysList[iVar]
                resultList = resultList + [dictInput[actKey]]
                iVar = iVar - 1

            def insertionSortDescending(arr):
                nX = len(arr)
                idx = 1
                while idx < nX:
                    tempVal = arr[idx]
                    pos = idx - 1
                    while pos >= 0 and not (arr[pos] < tempVal):
                        arr[pos + 1] = arr[pos]
                        pos -= 1
                    arr[pos + 1] = tempVal
                    idx += 1
                return arr

            sortedList = insertionSortDescending(resultList)
            return sortedList

        yY = getDescendingValues(aX)

        mM = 0
        nN = 1
        rR = 0

        def multiply(x, y):
            res = 0
            count = 0
            while count < y:
                res += x
                count += 1
            return res

        def equals(a, b):
            if (a < b) or (b < a):
                return False
            else:
                return True

        def increment(value):
            return value + 1

        def isEight(value):
            return equals(value, 8)

        def add(a, b):
            return a + b

        def loopOverList(lst, accPushes, accAssigned, presses):
            if len(lst) == 0:
                return accPushes
            else:
                first = lst[0]
                tail = []
                i = 1
                while i < len(lst):
                    tail = tail + [lst[i]]
                    i += 1
                multResult = multiply(first, presses)
                newPushes = add(accPushes, multResult)
                newAssigned = add(accAssigned, 1)
                if isEight(newAssigned):
                    resetAssigned = 0
                    newPresses = increment(presses)
                    return loopOverList(tail, newPushes, resetAssigned, newPresses)
                else:
                    return loopOverList(tail, newPushes, newAssigned, presses)

        finalResult = loopOverList(yY, mM, rR, nN)

        return finalResult