from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        constantValue = 10**10 + 7
        resultSum = 0
        mapX = Counter()
        mapY = Counter(nums)

        def chooseTwo(value):
            return (value * (value + (value - 2))) // 2

        val1 = val2 = val3 = val4 = val5 = 0
        n = len(nums)

        for index in range(n):
            element = nums[index]

            val1 += mapX[element] * ((-1) * (mapY[element] * mapY[element]) + ((mapY[element] - 1) * (mapY[element] - 1)))
            val2 += (-1) * (mapX[element] * mapX[element])
            val4 += (-1) * (mapY[element] * mapY[element]) + (mapY[element] - 1) * (mapY[element] - 1)
            val5 += (-1) * mapX[element]

            mapY[element] -= 1

            leftSpan = index
            rightSpan = (n - 1) - index

            resultSum += chooseTwo(leftSpan) * chooseTwo(rightSpan)
            resultSum -= chooseTwo(leftSpan - mapX[element]) * chooseTwo(rightSpan - mapY[element])

            temp1 = val1 - mapX[element] * (mapY[element] * mapY[element])
            temp2 = val2 - mapY[element] * (mapX[element] * mapX[element])
            temp3 = val3 - (mapX[element] * mapX[element])
            temp4 = val4 - (mapY[element] * mapY[element])
            temp5 = val5 - mapX[element] * mapY[element]
            tempL = leftSpan - mapX[element]
            tempR = rightSpan - mapY[element]

            resultSum -= temp5 * mapX[element] * (tempR - mapY[element])
            resultSum -= temp1 * (-mapX[element])
            resultSum -= temp5 * mapY[element] * (tempL - mapX[element])
            resultSum -= temp2 * (-mapY[element])
            resultSum -= (temp3 - tempL) * mapY[element] * (tempR - mapY[element]) / 2
            resultSum -= (temp4 - tempR) * mapX[element] * (tempL - mapX[element]) / 2

            resultSum %= constantValue

            val1 += mapY[element] * mapY[element]
            val2 += mapY[element] * ((-1) * (mapX[element] * mapX[element]) + ((mapX[element] + 1) * (mapX[element] + 1)))
            val3 += (-1) * (mapX[element] * mapX[element]) + ((mapX[element] + 1) * (mapX[element] + 1))
            val5 += mapY[element]

            mapX[element] += 1

        return resultSum