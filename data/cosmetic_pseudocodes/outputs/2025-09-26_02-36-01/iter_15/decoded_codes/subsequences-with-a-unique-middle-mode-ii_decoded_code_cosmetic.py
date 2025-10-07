from collections import defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        constModulus = 10**9 + 7
        resultCounter = 0
        leftFreq = defaultdict(int)
        rightFreq = defaultdict(int)

        for element in nums:
            rightFreq[element] += 1

        def chooseTwo(x):
            return (x * (x - 1)) // 2 if x >= 2 else 0

        accPss = 0
        accSpp = 0
        accPp = 0
        sumSquaresS = 0
        accPs = 0

        for freqValue in rightFreq.values():
            sumSquaresS += freqValue * freqValue

        indexPosition = 0
        n = len(nums)
        while indexPosition < n:
            currentVal = nums[indexPosition]
            decrementSVal = rightFreq[currentVal]
            incrementPVal = leftFreq[currentVal]

            accPss += incrementPVal * ((-decrementSVal * decrementSVal) + ((decrementSVal - 1) * (decrementSVal - 1)))
            accSpp += -incrementPVal * incrementPVal
            sumSquaresS += (-decrementSVal * decrementSVal) + ((decrementSVal - 1) * (decrementSVal - 1))
            accPs += -incrementPVal

            rightFreq[currentVal] -= 1

            leftCount = indexPosition
            rightCount = n - indexPosition - 1

            tempVal1 = chooseTwo(leftCount) * chooseTwo(rightCount)
            tempVal2 = chooseTwo(leftCount - incrementPVal) * chooseTwo(rightCount - rightFreq[currentVal])

            resultCounter += tempVal1 - tempVal2

            tempPssMinus = accPss - (incrementPVal * (rightFreq[currentVal] * rightFreq[currentVal]))
            tempSppMinus = accSpp - (rightFreq[currentVal] * (incrementPVal * incrementPVal))
            tempPpMinus = accPp - (incrementPVal * incrementPVal)
            tempSsMinus = sumSquaresS - (rightFreq[currentVal] * rightFreq[currentVal])
            tempPsMinus = accPs - (incrementPVal * rightFreq[currentVal])

            adjustedP = (leftCount - incrementPVal)
            adjustedS = (rightCount - rightFreq[currentVal])

            decr1 = tempPsMinus * incrementPVal * (rightCount - rightFreq[currentVal]) + tempPssMinus * (-incrementPVal)
            decr2 = tempPsMinus * rightFreq[currentVal] * (leftCount - incrementPVal) + tempSppMinus * (-rightFreq[currentVal])
            decr3 = (tempPpMinus - adjustedP) * rightFreq[currentVal] * (rightCount - rightFreq[currentVal]) // 2
            decr4 = (tempSsMinus - adjustedS) * incrementPVal * (leftCount - incrementPVal) // 2

            resultCounter -= (decr1 + decr2 + decr3 + decr4)
            resultCounter %= constModulus

            accPss += rightFreq[currentVal] * rightFreq[currentVal]
            accSpp += (rightFreq[currentVal] * (-incrementPVal * incrementPVal)) + ((incrementPVal + 1) * (incrementPVal + 1))
            accPp += (-(incrementPVal * incrementPVal)) + ((incrementPVal + 1) * (incrementPVal + 1))
            accPs += rightFreq[currentVal]

            leftFreq[currentVal] += 1
            indexPosition += 1

        return resultCounter