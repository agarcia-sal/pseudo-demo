class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            alpha = arr[0]
            beta = arr[0]
            indexGamma = 1
            while indexGamma < len(arr):
                delta = arr[indexGamma]
                if not (delta <= alpha + delta):
                    alpha = delta
                else:
                    alpha = alpha + delta
                if beta < alpha:
                    beta = alpha
                indexGamma += 1
            return beta

        omega = kadane(nums)
        sigmaSet = {omegaElement for omegaElement in nums}

        sigmaList = list(sigmaSet)

        iota = 0
        while iota < len(sigmaList):
            kappa = sigmaList[iota]
            lambdaList = []
            zetaIndex = 0
            while zetaIndex < len(nums):
                mu = nums[zetaIndex]
                if not (mu == kappa):
                    lambdaList.append(mu)
                zetaIndex += 1
            if len(lambdaList) > 0:
                newSum = kadane(lambdaList)
                if omega < newSum:
                    omega = newSum
            iota += 1

        return omega