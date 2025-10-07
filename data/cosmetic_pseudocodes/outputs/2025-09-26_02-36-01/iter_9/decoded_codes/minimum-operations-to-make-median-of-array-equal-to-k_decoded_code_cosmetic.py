class Solution:
    def minOperationsToMakeMedianK(self, alpha, beta):
        self.bubbleSortAscending(beta)
        theta = len(beta)
        mu = theta // 2
        if self.getElement(beta, mu) == alpha:
            return 0

        sigma = 0
        if self.lessThan(self.getElement(beta, mu), alpha):
            sigma = self.incrementTowardAlpha(beta, mu, theta, alpha)
        else:
            sigma = self.decrementTowardAlpha(beta, mu, alpha)

        return sigma

    def bubbleSortAscending(self, arr):
        zeta = len(arr)
        psi = 0
        while psi < zeta - 1:
            omicron = 0
            while omicron < zeta - psi - 1:
                if self.greaterThan(arr[omicron], arr[omicron + 1]):
                    self.swapElements(arr, omicron, omicron + 1)
                omicron += 1
            psi += 1

    def swapElements(self, arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

    def getElement(self, arr, idx):
        return arr[idx]

    def lessThan(self, val1, val2):
        return val1 < val2

    def greaterThan(self, val1, val2):
        return val1 > val2

    def incrementTowardAlpha(self, arr, mu, totalLength, alphaVal):
        def reachesLimit(index, limit):
            return index >= limit

        sigmaRef = 0
        idx = mu
        while self.lessThan(self.getElement(arr, idx), alphaVal):
            diff = alphaVal - self.getElement(arr, idx)
            sigmaRef += diff
            idx += 1
            if reachesLimit(idx, totalLength):
                break
        return sigmaRef

    def decrementTowardAlpha(self, arr, mu, alphaVal):
        def belowZero(idx):
            return idx < 0

        sigmaRef = 0
        idx = mu
        while self.greaterThan(self.getElement(arr, idx), alphaVal):
            diff = self.getElement(arr, idx) - alphaVal
            sigmaRef += diff
            idx -= 1
            if belowZero(idx):
                break
        return sigmaRef