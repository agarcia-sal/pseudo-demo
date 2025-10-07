from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def helperSwap(arr, idx1, idx2):
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

        nums.sort()

        totalCount = 0
        frequencyMap = defaultdict(int)

        def computeVis(index, maxIndex, currArr, visited):
            if index >= maxIndex:
                return

            def innerLoop(i, j, arrRef, setRef):
                if i < 0:
                    return
                helperSwap(arrRef, i, j)
                combinedNumStr = ''.join(arrRef)
                combinedNumVal = int(combinedNumStr)
                setRef.add(combinedNumVal)

                def nestedLoops(startQ, limitQ, startP, limitP, arrayRef, setRefInner):
                    if startQ > limitQ:
                        return
                    if startP >= limitP:
                        nestedLoops(startQ + 1, limitQ, startQ + 1, limitP, arrayRef, setRefInner)
                        return
                    helperSwap(arrayRef, startP, startQ)
                    tmpConcat = ''.join(arrayRef)
                    intValTmp = int(tmpConcat)
                    setRefInner.add(intValTmp)
                    helperSwap(arrayRef, startP, startQ)

                    nestedLoops(startQ, limitQ, startP + 1, limitP, arrayRef, setRefInner)

                nestedLoops(i + 1, maxIndex - 1, i + 1, maxIndex - 1, arrRef, setRef)
                helperSwap(arrRef, i, j)

                innerLoop(i - 1, j, arrRef, setRef)

            innerLoop(index - 1, index, currArr, visited)
            computeVis(index + 1, maxIndex, currArr, visited)

        def processNumber(originalNum):
            visitedSet = set()
            stringifiedNum = list(str(originalNum))
            lengthVal = len(stringifiedNum)

            computeVis(0, lengthVal, stringifiedNum, visitedSet)
            return visitedSet

        def iterateNumbers(pos, numbersList, freqDict, acc):
            if pos >= len(numbersList):
                return acc

            currentNumber = numbersList[pos]
            visitedNums = processNumber(currentNumber)
            interimSum = 0
            for val in visitedNums:
                interimSum += freqDict[val]
            acc += interimSum
            freqDict[currentNumber] += 1

            return iterateNumbers(pos + 1, numbersList, freqDict, acc)

        result = iterateNumbers(0, nums, frequencyMap, 0)
        return result