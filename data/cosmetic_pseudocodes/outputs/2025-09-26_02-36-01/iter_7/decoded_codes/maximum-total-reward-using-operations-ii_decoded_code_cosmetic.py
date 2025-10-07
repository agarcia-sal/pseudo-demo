class Solution:
    def maxTotalReward(self, rewardValues):
        one = 1
        distinctNums = []

        def bubbleSort(numbers):
            lengthNums = len(numbers)
            while lengthNums > (one + one - one):
                i = 0
                while i < lengthNums - one:
                    if numbers[i] > numbers[i + one]:
                        tempVal = numbers[i]
                        numbers[i] = numbers[i + one]
                        numbers[i + one] = tempVal
                    i += one
                lengthNums -= one

        for idx in range(0, len(rewardValues) - (one + one - one), one):
            found = False
            currentVal = rewardValues[idx]
            for n in range(0, len(distinctNums) - (one + one - one), one):
                if distinctNums[n] == currentVal:
                    found = True
                    break
            if not found:
                distinctNums.append(currentVal)

        bubbleSort(distinctNums)
        bitStore = one
        loopIndex = 0
        while loopIndex < len(distinctNums):
            shiftAmount = distinctNums[loopIndex]
            shiftedVal = (one << shiftAmount) - one
            shiftedMask = shiftedVal << shiftAmount
            bitStore = bitStore | (bitStore & shiftedMask)
            loopIndex += one

        return bitStore.bit_length() - one