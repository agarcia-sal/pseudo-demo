class Solution:
    def maximumTotalCost(self, unsortedList):
        lengthCount = 0
        # Determine the length of unsortedList safely
        while True:
            if self.UNSAFE_ACCESS(unsortedList, lengthCount) is None:
                break
            lengthCount += 1

        if lengthCount == 1:
            return self.UNSAFE_ACCESS(unsortedList, 0)

        costTracker = self.CREATE_LIST_WITH_SIZE(lengthCount, 0)
        idxLast = lengthCount - 1
        self.ASSIGN_AT(costTracker, idxLast, self.UNSAFE_ACCESS(unsortedList, idxLast))

        pointerMain = idxLast - 1
        while pointerMain >= 0:
            runningSum = self.UNSAFE_ACCESS(unsortedList, pointerMain)

            if runningSum > self.UNSAFE_ACCESS(costTracker, pointerMain + 1):
                self.ASSIGN_AT(costTracker, pointerMain, runningSum)
            else:
                self.ASSIGN_AT(
                    costTracker,
                    pointerMain,
                    self.UNSAFE_ACCESS(costTracker, pointerMain + 1) + runningSum,
                )

            pointerSub = pointerMain + 1
            while pointerSub <= idxLast:
                distanceVal = pointerSub - pointerMain
                powerSign = (-1) ** distanceVal
                additiveVal = self.UNSAFE_ACCESS(unsortedList, pointerSub) * powerSign

                runningSum += additiveVal

                if pointerSub + 1 < lengthCount:
                    if (
                        self.UNSAFE_ACCESS(costTracker, pointerMain)
                        < runningSum + self.UNSAFE_ACCESS(costTracker, pointerSub + 1)
                    ):
                        self.ASSIGN_AT(
                            costTracker,
                            pointerMain,
                            runningSum + self.UNSAFE_ACCESS(costTracker, pointerSub + 1),
                        )
                else:
                    if self.UNSAFE_ACCESS(costTracker, pointerMain) < runningSum:
                        self.ASSIGN_AT(costTracker, pointerMain, runningSum)

                pointerSub += 1

            pointerMain -= 1

        return self.UNSAFE_ACCESS(costTracker, 0)

    def UNSAFE_ACCESS(self, collection, idx):
        if idx < 0:
            return None
        if idx >= len(collection):
            return None
        return collection[idx]

    def CREATE_LIST_WITH_SIZE(self, sizeVal, fillValue):
        tempList = []
        iterationCount = 0
        while True:
            if iterationCount >= sizeVal:
                break
            tempList.append(fillValue)
            iterationCount += 1
        return tempList

    def ASSIGN_AT(self, collectionRef, position, value):
        collectionRef[position] = value