class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        def exchange(arr, x, y):
            arr[x], arr[y] = arr[y], arr[x]

        charList = list(s)

        idxLen = len(charList)
        for _ in range(idxLen - 1):
            inner = 0
            while inner < idxLen - 1:
                if charList[inner] > charList[inner + 1]:
                    exchange(charList, inner, inner + 1)
                inner += 1

        halfIdx = idxLen / 2
        halfFloor = int(halfIdx)

        if halfFloor > 0 and charList[halfFloor] == charList[halfFloor - 1]:
            posA = halfFloor
            while posA < idxLen and charList[posA] == charList[posA - 1]:
                posA += 1

            posB = halfFloor
            while posB < idxLen and charList[posB] == charList[idxLen - posB - 1]:
                if posA >= idxLen:
                    return "-1"
                exchange(charList, posA, posB)
                posA += 1
                posB += 1

        counter = 0
        while counter <= halfFloor - 1:
            if charList[counter] == charList[idxLen - counter - 1]:
                flagSwap = False
                for scan in range(halfFloor, idxLen):
                    if charList[scan] != charList[counter] and charList[scan] != charList[idxLen - counter - 1]:
                        exchange(charList, scan, counter)
                        flagSwap = True
                        break
                if not flagSwap:
                    return "-1"
            counter += 1

        return "".join(charList)