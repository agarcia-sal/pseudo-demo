from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        modulus = 10**9 + 7
        freqMap = defaultdict(int)
        sumMap = defaultdict(int)

        def processIndex(index):
            if index >= len(nums):
                return
            current = nums[index]

            freqMap[current] += 1
            sumMap[current] += current

            sumMap[current] = (sumMap[current]
                + sumMap[current - 1]
                + freqMap[current - 1] * current) % modulus

            freqMap[current] = (freqMap[current] + freqMap[current - 1]) % modulus

            sumMap[current] = (sumMap[current]
                + sumMap[current + 1]
                + freqMap[current + 1] * current) % modulus

            freqMap[current] = (freqMap[current] + freqMap[current + 1]) % modulus

            processIndex(index + 1)

        processIndex(0)

        accumulator = sum(sumMap.values())
        return (accumulator % modulus + modulus) % modulus