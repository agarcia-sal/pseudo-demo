class Solution:
    def minMoves(self, quaxo):
        def absVal(x):
            return -x if x < 0 else x

        def lenSeq(sq):
            cnt = 0
            ptr = 0
            while ptr < len(sq):
                cnt += 1
                ptr += 1
            return cnt

        def sortByFirst(elmList):
            if lenSeq(elmList) < 2:
                return elmList
            pivot = elmList[0]
            lessPart = []
            greaterPart = []
            i = 1
            while i < lenSeq(elmList):
                if elmList[i][0] <= pivot[0]:
                    lessPart.append(elmList[i])
                else:
                    greaterPart.append(elmList[i])
                i += 1
            return sortByFirst(lessPart) + [pivot] + sortByFirst(greaterPart)

        def sortBySecond(elmList):
            if lenSeq(elmList) < 2:
                return elmList
            pivot = elmList[0]
            lessPart = []
            greaterPart = []
            i = 1
            while i < lenSeq(elmList):
                if elmList[i][1] <= pivot[1]:
                    lessPart.append(elmList[i])
                else:
                    greaterPart.append(elmList[i])
                i += 1
            return sortBySecond(lessPart) + [pivot] + sortBySecond(greaterPart)

        def calcAbsDiffSum(sortedList, posIdx, whichCoord):
            def loopSum(counter, acc):
                if counter >= lenSeq(sortedList):
                    return acc
                coordVal = sortedList[counter][whichCoord]
                diffVal = coordVal - counter
                if diffVal < 0:
                    diffVal = -diffVal
                return loopSum(counter + 1, acc + diffVal)
            return loopSum(0, 0)

        sizeN = lenSeq(quaxo)
        rowSorted = sortByFirst(quaxo)
        colSorted = sortBySecond(quaxo)
        sumRow = calcAbsDiffSum(rowSorted, 0, 0)
        sumCol = calcAbsDiffSum(colSorted, 0, 1)

        return sumRow + sumCol