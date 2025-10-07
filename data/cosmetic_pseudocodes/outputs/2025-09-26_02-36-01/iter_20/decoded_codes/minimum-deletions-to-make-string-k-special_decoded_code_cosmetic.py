class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def tallyChars(seq):
            dictX = {}
            posX = 0
            while True:
                if posX >= len(seq):
                    break
                ch = seq[posX]
                if ch in dictX:
                    dictX[ch] += 1
                else:
                    dictX[ch] = 1
                posX += 1
            return dictX

        def sortAscending(arr):
            def swap(arrA, idxA, idxB):
                arrA[idxA], arrA[idxB] = arrA[idxB], arrA[idxA]
            nX = len(arr)
            changed = True
            while changed:
                changed = False
                pX = 0
                while pX < nX - 1:
                    if arr[pX] > arr[pX + 1]:
                        swap(arr, pX, pX + 1)
                        changed = True
                    pX += 1
            return arr

        freqMap = tallyChars(word)
        freqList = []
        for key in freqMap:
            freqList.append(freqMap[key])
        freqList = sortAscending(freqList)

        minDel = float('inf')
        iY = 0
        while iY < len(freqList):
            maxAllow = freqList[iY] + k
            countDel = 0
            jY = iY + 1
            while jY < len(freqList):
                excess = freqList[jY] - maxAllow
                if excess > 0:
                    countDel += excess
                jY += 1
            mY = 0
            while mY < iY:
                countDel += freqList[mY]
                mY += 1
            if countDel < minDel:
                minDel = countDel
            iY += 1

        return minDel