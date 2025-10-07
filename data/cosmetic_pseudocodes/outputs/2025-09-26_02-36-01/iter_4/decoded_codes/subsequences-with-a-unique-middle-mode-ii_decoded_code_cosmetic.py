from collections import defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        modulo = 10**9 + 7
        totalCount = 0
        prefixCounter = defaultdict(int)
        suffixCounter = defaultdict(int)

        for e in nums:
            suffixCounter[e] += 1

        def combin2(x):
            # Combination of x choose 2 = x*(x-1)//2
            return x * (x - 1) // 2

        prefixSuffixSum = 0
        suffixPrefixProduct = 0
        prefixPrefixSum = 0
        suffixSquareSum = 0
        prefixSuffixCount = 0

        for freq in suffixCounter.values():
            suffixSquareSum += freq * freq

        index = 0
        n = len(nums)

        while index < n:
            currentVal = nums[index]

            valPrefixFreq = prefixCounter[currentVal]
            valSuffixFreq = suffixCounter[currentVal]

            deltaPSS1 = valPrefixFreq * ((valSuffixFreq - 1) * (valSuffixFreq - 1) - (valSuffixFreq * valSuffixFreq))
            deltaPSS2 = valPrefixFreq
            prefixSuffixSum += deltaPSS1 + deltaPSS2

            suffixPrefixProduct -= valPrefixFreq * valPrefixFreq

            deltaSS1 = (valSuffixFreq - 1) * (valSuffixFreq - 1) - (valSuffixFreq * valSuffixFreq)
            suffixSquareSum += deltaSS1

            prefixSuffixCount -= valPrefixFreq

            suffixCounter[currentVal] = valSuffixFreq - 1

            leftCount = index
            rightCount = n - index - 1

            combLeft = combin2(leftCount)
            combRight = combin2(rightCount)

            totalCount += combLeft * combRight

            modLeft = leftCount - valPrefixFreq
            modRight = rightCount - suffixCounter[currentVal]

            totalCount -= combin2(modLeft) * combin2(modRight)

            tempPSS = prefixSuffixSum - valPrefixFreq * (valSuffixFreq * valSuffixFreq)
            tempSPP = suffixPrefixProduct - suffixCounter[currentVal] * (valPrefixFreq * valPrefixFreq)
            tempPP = prefixPrefixSum - (valPrefixFreq * valPrefixFreq)
            tempSS = suffixSquareSum - (suffixCounter[currentVal] * suffixCounter[currentVal])
            tempPS = prefixSuffixCount - valPrefixFreq * suffixCounter[currentVal]
            modP = leftCount - valPrefixFreq
            modS = rightCount - suffixCounter[currentVal]

            part1 = tempPS * valPrefixFreq * (rightCount - suffixCounter[currentVal])
            part2 = tempPSS * (-valPrefixFreq)
            totalCount -= (part1 + part2)

            part3 = tempPS * suffixCounter[currentVal] * (leftCount - valPrefixFreq)
            part4 = tempSPP * (-suffixCounter[currentVal])
            totalCount -= (part3 + part4)

            part5 = (tempPP - modP) * suffixCounter[currentVal] * (rightCount - suffixCounter[currentVal])
            part5div_TWO = part5 // 2
            totalCount -= part5div_TWO

            part6 = (tempSS - modS) * valPrefixFreq * (leftCount - valPrefixFreq)
            part6div_TWO = part6 // 2
            totalCount -= part6div_TWO

            totalCount %= modulo

            squareValSuffix = valSuffixFreq * valSuffixFreq
            prefixSuffixSum += squareValSuffix

            incSPP = valSuffixFreq * (-valPrefixFreq * valPrefixFreq)
            surplus = (valPrefixFreq + 1) * (valPrefixFreq + 1)
            suffixPrefixProduct += incSPP + surplus

            prefixPrefixSum += (-valPrefixFreq * valPrefixFreq + (valPrefixFreq + 1) * (valPrefixFreq + 1))

            prefixSuffixCount += valSuffixFreq

            prefixCounter[currentVal] = valPrefixFreq + 1

            index += 1

        return totalCount % modulo