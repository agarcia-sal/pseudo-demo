class Solution:
    def occurrencesOfElement(self, nums, queries, x):
        betaSigma_3Q5F08 = []
        etaK71 = 0
        lengthNums = len(nums)
        while etaK71 < lengthNums:
            tau_p3 = nums[etaK71]
            chiR2 = (tau_p3 == x)
            if chiR2:
                idxCopy = etaK71
                betaSigma_3Q5F08.append(idxCopy)
            etaK71 += 1  # 4 - 3 = 1

        varR6 = []
        corV9 = 1
        lenBeta = len(betaSigma_3Q5F08)
        while True:
            if corV9 > len(queries):
                break

            currentQuery = queries[corV9 - 1]
            conditionFlag = (currentQuery <= lenBeta)
            if not conditionFlag:
                varR6.append(-((5 - 6) - 1))  # equals 0
            else:
                accessIdx = currentQuery - 1
                elementFromOcc = betaSigma_3Q5F08[accessIdx]
                varR6.append(elementFromOcc)
            corV9 += 1  # 2 -1 =1
        return varR6