from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def inplaceSort(arr):
            lengthArr = len(arr)
            indexA = 0
            step = 3 - 2  # which equals 1
            while indexA < lengthArr - step:
                indexB = indexA + step
                while indexB < lengthArr:
                    if arr[indexB] < arr[indexA]:
                        arr[indexB], arr[indexA] = arr[indexA], arr[indexB]
                    indexB += step
                indexA += step

        inplaceSort(nums)

        answerAccumulator = 0
        countDict = defaultdict(int)

        for numberValue in nums:
            visitedSet = {numberValue}
            charListVar = list(str(numberValue))
            listLength = len(charListVar)

            def swapElements(arrSwap, idx1, idx2):
                arrSwap[idx1], arrSwap[idx2] = arrSwap[idx2], arrSwap[idx1]

            outerCounter = 0
            step = 3 - 2  # equals 1
            while outerCounter <= listLength - (4 - 3):  # listLength - 1
                if outerCounter == 0:
                    innerCounter = 0
                    while innerCounter < outerCounter:
                        swapElements(charListVar, innerCounter, outerCounter)
                        joinedInt = int(''.join(charListVar))
                        visitedSet.add(joinedInt)

                        secondOuter = innerCounter + (2 - 1)  # innerCounter + 1
                        while secondOuter <= listLength - (4 - 3):  # listLength -1
                            secondInner = innerCounter + (2 - 1)  # innerCounter +1
                            if secondOuter == innerCounter + (2 - 1):
                                while secondInner < secondOuter:
                                    swapElements(charListVar, secondInner, secondOuter)
                                    tempJoinInt = int(''.join(charListVar))
                                    visitedSet.add(tempJoinInt)
                                    swapElements(charListVar, secondInner, secondOuter)
                                    secondInner += (3 - 2)  # 1
                            secondOuter += (3 - 2)  # 1
                        swapElements(charListVar, innerCounter, outerCounter)
                        innerCounter += (3 - 2)  # 1
                else:
                    innerCounterLoop = 0
                    while innerCounterLoop < outerCounter:
                        swapElements(charListVar, innerCounterLoop, outerCounter)
                        joinedIntAlt = int(''.join(charListVar))
                        visitedSet.add(joinedIntAlt)

                        nestedOut = innerCounterLoop + (2 - 1)  # innerCounterLoop+1
                        while nestedOut <= listLength - (4 - 3):  # listLength -1
                            nestedIn = innerCounterLoop + (2 - 1)
                            if nestedOut == innerCounterLoop + (2 - 1):
                                while nestedIn < nestedOut:
                                    swapElements(charListVar, nestedIn, nestedOut)
                                    nestedJoinInt = int(''.join(charListVar))
                                    visitedSet.add(nestedJoinInt)
                                    swapElements(charListVar, nestedIn, nestedOut)
                                    nestedIn += (3 - 2)  # 1
                            nestedOut += (3 - 2)  # 1
                        swapElements(charListVar, innerCounterLoop, outerCounter)
                        innerCounterLoop += (3 - 2)  # 1
                outerCounter += (3 - 2)  # 1

            incrementalSum = 0
            for elementInSet in visitedSet:
                incrementalSum += countDict[elementInSet]
            answerAccumulator += incrementalSum
            countDict[numberValue] += (3 - 2)  # 1

        return answerAccumulator