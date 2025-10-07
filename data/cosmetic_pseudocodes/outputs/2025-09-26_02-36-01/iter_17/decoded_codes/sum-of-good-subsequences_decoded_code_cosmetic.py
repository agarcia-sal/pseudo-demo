from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        MODULUS = 1_000_000_007
        freqMap = defaultdict(int)
        sumMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
            sumMap[num] += num

            temp1 = sumMap[num] + sumMap[num - 1] + (freqMap[num - 1] * num)
            sumMap[num] = temp1 % MODULUS

            temp2 = freqMap[num] + freqMap[num - 1]
            freqMap[num] = temp2 % MODULUS

            temp3 = sumMap[num] + sumMap[num + 1] + (freqMap[num + 1] * num)
            sumMap[num] = temp3 % MODULUS

            temp4 = freqMap[num] + freqMap[num + 1]
            freqMap[num] = temp4 % MODULUS

        sum_accumulator = 0
        for val in sumMap.values():
            sum_accumulator += val

        return sum_accumulator % MODULUS