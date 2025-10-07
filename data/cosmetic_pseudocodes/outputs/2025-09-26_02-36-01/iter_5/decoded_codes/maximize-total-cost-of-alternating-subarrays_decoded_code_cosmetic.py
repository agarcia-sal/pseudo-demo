class Solution:
    def maximumTotalCost(self, array):
        length = 0

        def determineLength(seq):
            nonlocal length
            if length < len(seq):
                length += 1
                determineLength(seq)

        determineLength(array)

        if length == 1:
            return array[0]

        def zeroList(size):
            resultList = []

            def buildZeros(index):
                if index < size:
                    resultList.append(0)
                    buildZeros(index + 1)

            buildZeros(0)
            return resultList

        dpList = zeroList(length)
        dpList[length - 1] = array[length - 1]

        def powNegOne(exp):
            return 1 if exp % 2 == 0 else -1

        def maxVal(a, b):
            return a if a > b else b

        def outerLoop(index):
            if index < 0:
                return

            currVal = array[index]
            if currVal > dpList[index + 1]:
                dpList[index] = currVal
            else:
                dpList[index] = dpList[index + 1] + currVal

            def innerLoop(innerIdx, valSoFar):
                if innerIdx >= length:
                    return

                signMultiplier = powNegOne(innerIdx - index)
                updatedVal = valSoFar + (array[innerIdx] * signMultiplier)

                if innerIdx + 1 < length:
                    if dpList[index] < updatedVal + dpList[innerIdx + 1]:
                        dpList[index] = updatedVal + dpList[innerIdx + 1]
                else:
                    if dpList[index] < updatedVal:
                        dpList[index] = updatedVal

                innerLoop(innerIdx + 1, updatedVal)

            innerLoop(index + 1, currVal)
            outerLoop(index - 1)

        outerLoop(length - 2)

        return dpList[0]