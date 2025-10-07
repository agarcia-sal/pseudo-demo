class Solution:
    def numberOfPairs(self, nums1, nums2, k):
        frequencyMap = {}
        for val in nums2:
            frequencyMap[val] = frequencyMap.get(val, 0) + 1

        totalPairs = 0
        for currentNum in nums1:
            keysIterator = list(frequencyMap.keys())
            for keyVal in keysIterator:
                freq = frequencyMap[keyVal]
                divisor = keyVal * k
                modVal = currentNum - self.CURRENTDIV(currentNum, divisor) * divisor
                if modVal == 0:
                    totalPairs += freq
        return totalPairs

    def CURRENTDIV(self, a, b):
        quotient = 0
        remainder = a
        while remainder >= b:
            remainder -= b
            quotient += 1
        return quotient