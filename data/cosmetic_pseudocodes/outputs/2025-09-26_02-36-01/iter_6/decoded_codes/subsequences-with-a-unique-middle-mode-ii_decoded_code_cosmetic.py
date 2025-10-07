class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MODULO_VAL = 10_000_000_007

        resultSum = 0
        firstCounter = dict()
        secondCounter = dict()

        def incrementKey(dictMap, key):
            dictMap[key] = dictMap.get(key, 0) + 1

        def decrementKey(dictMap, key):
            dictMap[key] = dictMap.get(key, 0) - 1

        def nChoose2(x):
            return (x * (x - 1)) // 2 if x >= 0 else 0

        for num in nums:
            incrementKey(secondCounter, num)

        tempPss = 0
        tempSpp = 0
        tempPp = 0
        tempSs = 0
        tempPs = 0

        valsList = list(secondCounter.keys())

        # tempSs = sum of freq^2 for all elements
        for elem in valsList:
            freq = secondCounter[elem]
            tempSs += freq * freq

        currentIndex = 0
        n = len(nums)

        while currentIndex < n:
            val = nums[currentIndex]
            firstFreq = firstCounter.get(val, 0)
            secondFreq = secondCounter.get(val, 0)

            temp1 = (-firstFreq) * (secondFreq * secondFreq)
            temp2 = (-firstFreq) * ((secondFreq - 1) * (secondFreq - 1))
            temp3 = -(firstFreq * firstFreq)
            temp4 = -(secondFreq * secondFreq)
            temp5 = -firstFreq
            temp6 = -(firstFreq * firstFreq)
            temp7 = (firstFreq + 1) * (firstFreq + 1)
            temp8 = -(secondFreq * secondFreq)
            temp9 = (secondFreq - 1) * (secondFreq - 1)
            temp10 = (secondFreq * (- (firstFreq * firstFreq)) + temp7)

            tempPss += temp2 + temp1 + secondFreq
            tempSpp += temp3
            tempSs += temp4 + temp9
            tempPs += temp5

            decrementKey(secondCounter, val)

            lenLeft = currentIndex
            lenRight = n - currentIndex - 1

            addVal1 = nChoose2(lenLeft) * nChoose2(lenRight)
            addVal2 = nChoose2(lenLeft - firstFreq) * nChoose2(lenRight - secondFreq)
            pssAdj = tempPss - (firstFreq * (secondFreq * secondFreq))
            sppAdj = tempSpp - (secondFreq * (firstFreq * firstFreq))
            ppAdj = tempPp - (firstFreq * firstFreq)
            ssAdj = tempSs - (secondFreq * secondFreq)
            psAdj = tempPs - (firstFreq * secondFreq)
            pAdj = lenLeft - firstFreq
            sAdj = lenRight - secondFreq

            decVal1 = (psAdj * firstFreq * (lenRight - secondFreq)) + (pssAdj * (- firstFreq))
            decVal2 = (psAdj * secondFreq * (lenLeft - firstFreq)) + (sppAdj * (- secondFreq))
            decVal3 = ((ppAdj - pAdj) * secondFreq * (lenRight - secondFreq)) // 2
            decVal4 = ((ssAdj - sAdj) * firstFreq * (lenLeft - firstFreq)) // 2

            resultSum += addVal1 - addVal2 - decVal1 - decVal2 - decVal3 - decVal4
            resultSum %= MODULO_VAL

            tempPss += secondFreq * secondFreq
            tempSpp += secondFreq * (-(firstFreq * firstFreq)) + ((firstFreq + 1) * (firstFreq + 1))
            tempPp += (-(firstFreq * firstFreq) + ((firstFreq + 1) * (firstFreq + 1)))
            tempPs += secondFreq

            incrementKey(firstCounter, val)

            currentIndex += 1

        return resultSum