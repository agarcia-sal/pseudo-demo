class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isAlpha(chr: str) -> bool:
            return ('A' <= chr <= 'Z') or ('a' <= chr <= 'z')

        def toInt(chr: str) -> int:
            return ord(chr) - ord('0')

        def concatStrings(listStrings: list[str]) -> str:
            def concatHelper(index: int, acc: str) -> str:
                if index >= len(listStrings):
                    return acc
                return concatHelper(index + 1, acc + listStrings[index])
            return concatHelper(0, "")

        def sortedKeys(dictMap: dict[str, int]) -> list[str]:
            def sortRec(keysList: list[str], sortedList: list[str]) -> list[str]:
                if len(keysList) == 0:
                    return sortedList
                minChar = keysList[0]
                restChars = keysList[1:]
                leftSide = []
                rightSide = []
                for key in restChars:
                    if key < minChar:
                        rightSide.append(minChar)
                        minChar = key
                    else:
                        rightSide.append(key)
                return sortRec(rightSide, sortedList + [minChar])
            return sortRec(list(dictMap.keys()), [])

        def addCountToMap(mapLetters: dict[str, int], keyChar: str, amount: int) -> None:
            oldValue = mapLetters.get(keyChar, 0)
            mapLetters[keyChar] = oldValue + amount

        def processIndex(idx: int, currentChar: str, currentVal: int, mapLetters: dict[str, int]) -> dict[str, int]:
            if idx >= len(compressed):
                if currentChar != "":
                    addCountToMap(mapLetters, currentChar, currentVal)
                return mapLetters
            chr = compressed[idx]
            if isAlpha(chr):
                if currentChar != "":
                    addCountToMap(mapLetters, currentChar, currentVal)
                return processIndex(idx + 1, chr, 0, mapLetters)
            else:
                newVal = (currentVal * 10) + toInt(chr)
                return processIndex(idx + 1, currentChar, newVal, mapLetters)

        mapLetters = {}
        finalMap = processIndex(0, "", 0, mapLetters)

        lettersSorted = sortedKeys(finalMap)
        partsResult = []

        def buildParts(index: int, accum: list[str]) -> list[str]:
            if index >= len(lettersSorted):
                return accum
            c = lettersSorted[index]
            v = finalMap[c]
            part = c + str(v)
            return buildParts(index + 1, accum + [part])

        partsList = buildParts(0, [])
        resultString = concatStrings(partsList)
        return resultString