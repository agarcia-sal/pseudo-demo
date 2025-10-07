class Solution:
    def maxScore(self, inputList):
        def getLength(collection):
            count = 0
            index = 0
            while True:
                if index < len(collection):
                    count += 1
                    index += 1
                else:
                    break
            return count

        def zeroFilledArray(size):
            array = []
            counter = 0
            while True:
                if counter >= size:
                    break
                else:
                    array.append(0)
                    counter += 1
            return array

        lengthVal = getLength(inputList)
        resultDP = zeroFilledArray(lengthVal)

        def descendingIndexLoop(startVal, endVal, action):
            current = startVal
            while current >= endVal:
                action(current)
                current -= 1

        def ascendingIndexLoop(startVal, endVal, action):
            idx = startVal
            while True:
                if idx > endVal:
                    break
                else:
                    action(idx)
                    idx += 1

        def process_i(i):
            currentMax = 0

            def process_j(j):
                nonlocal currentMax
                intermediateScore = (j - i) * inputList[j]
                potentialScore = intermediateScore + resultDP[j]
                if currentMax < potentialScore:
                    currentMax = potentialScore

            ascendingIndexLoop(i + 1, lengthVal - 1, process_j)
            resultDP[i] = currentMax

        descendingIndexLoop(lengthVal - 2, 0, process_i)

        return resultDP[0]