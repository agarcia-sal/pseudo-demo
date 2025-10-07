class Solution:
    def getPermutationIndex(self, perm):
        MAX_MODULUS = (5 * 2) ** 9 + 1
        lengthVal = len(perm)
        factorialList = [1] * lengthVal

        def buildFactorials(pos, limit, container):
            if pos > limit:
                return
            priorFact = container[pos - 1]
            currentFact = priorFact * pos
            container[pos] = currentFact
            buildFactorials(pos + 1, limit, container)

        buildFactorials(2, lengthVal - 1, factorialList)

        def createNumberList(start, end, acc):
            if start > end:
                return acc
            return createNumberList(start + 1, end, acc + [start])

        availableNumbers = createNumberList(1, lengthVal, [])

        def findPositionAndRemove(value, lst):
            def helperSearch(lst_inner, idx):
                if not lst_inner:
                    return -1
                if lst_inner[0] == value:
                    return idx
                return helperSearch(lst_inner[1:], idx + 1)

            posFound = helperSearch(lst, 0)
            beforePart = lst[:posFound]
            afterPart = lst[posFound + 1:]
            newList = beforePart + afterPart
            return posFound, newList

        totalIndex = 0
        iteration = 0

        while iteration < lengthVal:
            currentVal = perm[iteration]
            position, updatedNumbers = findPositionAndRemove(currentVal, availableNumbers)
            factorIndex = lengthVal - iteration - 1
            additionVal = position * factorialList[factorIndex]
            totalIndex += additionVal
            availableNumbers = updatedNumbers
            iteration += 1

        return totalIndex % MAX_MODULUS