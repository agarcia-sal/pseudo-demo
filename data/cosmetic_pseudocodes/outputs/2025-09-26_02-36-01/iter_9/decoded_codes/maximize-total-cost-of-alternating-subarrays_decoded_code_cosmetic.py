class Solution:
    def maximumTotalCost(self, theta):
        def negOnePower(exp):
            return 1 if exp % 2 == 0 else -1

        lenVar = len(theta)

        if lenVar == 1:
            return theta[0]

        arrVar = [0] * lenVar
        arrVar[lenVar - 1] = theta[lenVar - 1]

        idxVar = lenVar - 2
        while idxVar >= 0:
            sumVar = theta[idxVar]
            if sumVar > arrVar[idxVar + 1]:
                arrVar[idxVar] = sumVar
            else:
                arrVar[idxVar] = arrVar[idxVar + 1] + sumVar

            innerIdx = idxVar + 1
            while innerIdx < lenVar:
                altSign = negOnePower(innerIdx - idxVar)
                sumVar += theta[innerIdx] * altSign

                if innerIdx + 1 < lenVar:
                    candidate = sumVar + arrVar[innerIdx + 1]
                    if arrVar[idxVar] < candidate:
                        arrVar[idxVar] = candidate
                else:
                    if arrVar[idxVar] < sumVar:
                        arrVar[idxVar] = sumVar

                innerIdx += 1
            idxVar -= 1

        return arrVar[0]