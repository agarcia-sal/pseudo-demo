class Solution:
    def beautifulIndices(self, s: str, x: str, y: str, z: int) -> list[int]:
        def findIndices(strParam: str, pattern: str, pos: int, acc: list[int]) -> list[int]:
            if pos > len(strParam) - len(pattern):
                return acc
            sliceStart = pos
            sliceEnd = pos + len(pattern)
            isMatch = False
            if strParam[sliceStart:sliceEnd] == pattern:
                isMatch = True
            newAcc = acc + [pos] if isMatch else acc
            return findIndices(strParam, pattern, pos + 1, newAcc)

        firstIndices = findIndices(s, x, 0, [])
        secondIndices = findIndices(s, y, 0, [])

        def mergeLists(listOne: list[int], listTwo: list[int], idxOne: int, idxTwo: int, kVal: int, resultList: list[int]) -> list[int]:
            if idxOne >= len(listOne) or idxTwo >= len(listTwo):
                return resultList
            firstVal = listOne[idxOne]
            secondVal = listTwo[idxTwo]
            diff = firstVal - secondVal
            absDiff = abs(diff)
            if absDiff <= kVal:
                return mergeLists(listOne, listTwo, idxOne + 1, idxTwo, kVal, resultList + [firstVal])
            elif firstVal < secondVal:
                return mergeLists(listOne, listTwo, idxOne + 1, idxTwo, kVal, resultList)
            else:
                return mergeLists(listOne, listTwo, idxOne, idxTwo + 1, kVal, resultList)

        finalIndices = mergeLists(firstIndices, secondIndices, 0, 0, z, [])
        return finalIndices