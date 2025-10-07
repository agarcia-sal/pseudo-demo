class Solution:
    def queryResults(self, paramA, paramB):
        def containsKey(container, key):
            for idxTemp in range(len(container)):
                if container[idxTemp][0] == key:
                    return True
            return False

        def getValue(container, key):
            for idxTmp in range(len(container)):
                if container[idxTmp][0] == key:
                    return container[idxTmp][1]
            return None

        def removeFromSet(setList, element):
            iVar = 0
            while iVar < len(setList):
                if setList[iVar] == element:
                    setList[iVar] = setList[-1]
                    setList.pop()
                    break
                iVar += 1

        def addToSet(setList, element):
            if not containsKey([(v, 0) for v in setList], element):  # Adjusted for value check
                setList.append(element)

        mapColors = []
        uniqueSet = []
        outputList = []

        def processQuery(recIdx):
            if recIdx >= len(paramB):
                return

            queryKey, queryVal = paramB[recIdx]

            if containsKey(mapColors, queryKey):
                previousColor = getValue(mapColors, queryKey)
                if previousColor in uniqueSet:
                    removeFromSet(uniqueSet, previousColor)

            updated = False
            for wIdx in range(len(mapColors)):
                if mapColors[wIdx][0] == queryKey:
                    mapColors[wIdx][1] = queryVal
                    updated = True
                    break
            if not updated:
                mapColors.append([queryKey, queryVal])

            if queryVal not in uniqueSet:
                uniqueSet.append(queryVal)

            outputList.append(len(uniqueSet))

            processQuery(recIdx + 1)

        processQuery(0)

        return outputList