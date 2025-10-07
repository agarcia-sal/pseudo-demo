class Solution:
    def maxTotalReward(self, rewardValues):
        def sortSequence(src, dest):
            if len(src) <= 1:
                dest.extend(src)
            else:
                midpoint = len(src) // 2
                leftPart = []
                rightPart = []
                sortSequence(src[0:midpoint], leftPart)
                sortSequence(src[midpoint:], rightPart)
                i, j = 0, 0
                merged = []
                while i < len(leftPart) or j < len(rightPart):
                    if j >= len(rightPart) or (i < len(leftPart) and not (rightPart[j] < leftPart[i])):
                        merged.append(leftPart[i])
                        i += 1
                    else:
                        merged.append(rightPart[j])
                        j += 1
                dest.extend(merged)

        def uniqueSortedElements(inputList, outputList):
            sortSequence(inputList, outputList)
            wq = 0
            while wq < len(outputList):
                wh = wq + 1
                while wh < len(outputList) and outputList[wq] == outputList[wh]:
                    wh += 1
                if (wh - wq) > 1:
                    # remove duplicates keeping one instance
                    del outputList[wq+1:wh]
                wq += 1

        def bitLength(num, resultRef):
            counter = 0
            remainder = num
            while remainder > 0:
                remainder //= 2
                counter += 1
            resultRef[0] = counter

        def helperShiftLeft(base, exponent):
            if exponent == 0:
                return 1
            else:
                return 2 * helperShiftLeft(base, exponent - 1)

        def iterateElements(lst, index, accRef):
            if index >= len(lst):
                return
            currentVal = lst[index]
            shiftedVal = helperShiftLeft(1, currentVal)
            maskVal = shiftedVal - 1
            accRef[0] = accRef[0] | ((accRef[0] & maskVal) * shiftedVal)
            iterateElements(lst, index + 1, accRef)

        tempList = []
        uniqueSortedElements(rewardValues, tempList)

        arg3 = 1
        cursor = 0

        accumulator = [arg3]
        iterateElements(tempList, 0, accumulator)

        bitlenResult = [0]
        bitLength(accumulator[0], bitlenResult)

        return bitlenResult[0] - 1