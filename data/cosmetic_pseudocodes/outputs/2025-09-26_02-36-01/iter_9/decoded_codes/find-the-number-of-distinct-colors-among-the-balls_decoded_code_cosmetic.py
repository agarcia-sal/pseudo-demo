class Solution:
    def queryResults(self, limitVal, queryList):
        def containsKey(dictRef, keyVal):
            return keyVal in dictRef

        def setDictValue(dictRef, keyVal, val):
            dictRef[keyVal] = val

        def addSetElement(setRef, element):
            setRef[element] = True

        def removeSetElement(setRef, element):
            if element in setRef:
                del setRef[element]

        def setSize(setRef):
            countValue = 0
            for _ in setRef:
                countValue += 1
            return countValue

        dictMapping = {}
        distinctSet = {}
        outcomeList = []
        indexCounter = 0

        def processIndex(i):
            if i >= limitVal:
                return

            keyId = queryList[i][0]
            colorId = queryList[i][1]

            if containsKey(dictMapping, keyId):
                priorClr = dictMapping[keyId]
                if priorClr in distinctSet:
                    removeSetElement(distinctSet, priorClr)

            setDictValue(dictMapping, keyId, colorId)
            addSetElement(distinctSet, colorId)

            outcomeList.append(setSize(distinctSet))

            processIndex(i + 1)

        processIndex(indexCounter)

        return outcomeList