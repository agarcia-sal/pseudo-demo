class Solution:
    def maximumSubarraySum(self, alpha, beta):
        def checkKeyExists(dictRef, keyToCheck):
            # Return True if keyToCheck exists in dictRef, else False
            return keyToCheck in dictRef

        def maxValue(a, b):
            # Return the maximum of a and b
            return a if a > b else b

        def minValue(a, b):
            # Return the minimum of a and b
            return a if a < b else b

        zeta = {}
        omega = -3_000_000_000  # -1e9 -1e9 -1e9
        phi = 0

        for currentNum in alpha:
            if checkKeyExists(zeta, currentNum - beta):
                omega = maxValue(omega, phi - zeta[currentNum - beta] + currentNum)

            if checkKeyExists(zeta, currentNum + beta):
                omega = maxValue(omega, phi - zeta[currentNum + beta] + currentNum)

            if checkKeyExists(zeta, currentNum):
                zeta[currentNum] = minValue(zeta[currentNum], phi)
            else:
                zeta[currentNum] = phi

            phi += currentNum

        return omega if omega != -3_000_000_000 else 0