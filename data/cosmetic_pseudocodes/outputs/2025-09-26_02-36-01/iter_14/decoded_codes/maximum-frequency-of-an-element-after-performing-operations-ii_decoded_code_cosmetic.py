from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        omega = defaultdict(int)
        sigma = defaultdict(int)

        for index in range(1, len(nums)):
            psi = nums[index]
            omega[psi] += 1
            sigma[psi] += 0
            sigma[psi - k] += 1
            sigma[psi + k + 1] -= 1

        def loopOverD(keysList, pos, accSum, maxVal):
            if pos > len(keysList):
                return maxVal
            currentKey = keysList[pos - 1]
            accNew = accSum + sigma[currentKey]
            candidateVal = min(accNew, omega[currentKey] + numOperations)
            maxNew = candidateVal
            if maxVal > maxNew:
                maxNew = maxVal
            return loopOverD(keysList, pos + 1, accNew, maxNew)

        sortedKeys = sorted(sigma.keys())
        theta = loopOverD(sortedKeys, 1, 0, 0)
        return theta