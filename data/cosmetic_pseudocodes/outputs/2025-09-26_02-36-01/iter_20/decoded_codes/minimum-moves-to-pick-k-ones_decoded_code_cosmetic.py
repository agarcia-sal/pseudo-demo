class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        def replicateList(size: int, output: list[int]) -> None:
            idx = 0
            while True:
                if idx >= size:
                    break
                output.append(0)
                idx += 1

        def appendToList(val: int, lst: list[int]) -> None:
            lst.append(val)

        tmpA = []
        ctrX = 0
        while ctrX < len(nums):
            if nums[ctrX] == 1:
                appendToList(ctrX, tmpA)
            ctrX += 1

        if len(tmpA) == 0:
            return k * 2

        lenA = len(tmpA)
        prefixArr = []
        replicateList(lenA + 1, prefixArr)

        indexP = 0
        while True:
            if indexP >= lenA:
                break
            prefixArr[indexP + 1] = prefixArr[indexP] + tmpA[indexP]
            indexP += 1

        def cost(l: int, r: int) -> int:
            halfLen = (l + r) // 2
            medVal = tmpA[halfLen]
            acc = 0
            varP = l
            while varP < halfLen:
                diffLeft = medVal - tmpA[varP] - halfLen + varP
                acc += diffLeft
                varP += 1
            varQ = halfLen + 1
            while varQ <= r:
                diffRight = tmpA[varQ] - medVal - varQ + halfLen
                acc += diffRight
                varQ += 1
            return acc

        minVal = 10**9
        startI = 0
        while startI <= lenA - k:
            endI = startI + k - 1
            sumCost = cost(startI, endI)

            if k % 2 == 1:
                midI = (startI + endI) // 2
                medX = tmpA[midI]
                chgNum = endI - midI - (medX - tmpA[midI] - 1)
            else:
                leftM = (startI + endI) // 2
                rightM = leftM + 1
                leftMed = tmpA[leftM]
                rightMed = tmpA[rightM]
                chgNum = rightM - leftM - 1 - (rightMed - leftMed - 1)

            if chgNum > maxChanges:
                sumCost += chgNum - maxChanges

            if sumCost < minVal:
                minVal = sumCost

            startI += 1

        return minVal