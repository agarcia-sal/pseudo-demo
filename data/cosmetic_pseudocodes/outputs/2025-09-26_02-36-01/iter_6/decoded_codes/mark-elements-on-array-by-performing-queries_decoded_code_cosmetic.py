from typing import List, Optional, Tuple, Set

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        def popMinHeap(hp: List[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
            if not hp:
                return None
            smallestValue, smallestIndex = hp[0]
            lastPos = len(hp) - 1
            hp[0] = hp[lastPos]
            hp.pop()
            currentPos = 0
            while True:
                leftChild = currentPos * 2 + 1
                rightChild = currentPos * 2 + 2
                minPos = currentPos

                if leftChild <= lastPos - 1 and hp[leftChild][0] < hp[minPos][0]:
                    minPos = leftChild
                if rightChild <= lastPos - 1 and hp[rightChild][0] < hp[minPos][0]:
                    minPos = rightChild

                if minPos == currentPos:
                    break
                hp[currentPos], hp[minPos] = hp[minPos], hp[currentPos]
                currentPos = minPos
            return smallestValue, smallestIndex

        def organizeHeap(listPairs: List[Tuple[int, int]]) -> None:
            lastIdx = len(listPairs) - 1
            i = (lastIdx - 1) // 2
            while i >= 0:
                parentPos = i
                while True:
                    leftChild = parentPos * 2 + 1
                    rightChild = parentPos * 2 + 2
                    minimumPos = parentPos

                    if leftChild <= lastIdx and listPairs[leftChild][0] < listPairs[minimumPos][0]:
                        minimumPos = leftChild
                    if rightChild <= lastIdx and listPairs[rightChild][0] < listPairs[minimumPos][0]:
                        minimumPos = rightChild

                    if minimumPos == parentPos:
                        break
                    listPairs[parentPos], listPairs[minimumPos] = listPairs[minimumPos], listPairs[parentPos]
                    parentPos = minimumPos
                i -= 1

        def totalSumOfList(aList: List[int]) -> int:
            accumulator = 0
            for val in aList:
                accumulator += val
            return accumulator

        aggregateSum = totalSumOfList(nums)

        heapList: List[Tuple[int, int]] = []
        positionHolder = 0
        n = len(nums)
        while positionHolder < n:
            heapList.append((nums[positionHolder], positionHolder))
            positionHolder += 1
        organizeHeap(heapList)

        outputList: List[int] = []

        def recursiveProcess(position: int, size: int, hpList: List[Tuple[int, int]],
                             markers: Set[int], runningSum: int,
                             outputAccumulator: List[int]) -> List[int]:
            if position >= size:
                return outputAccumulator
            currentQueryIndex, currentQueryNumber = queries[position]

            if currentQueryIndex not in markers:
                markers.add(currentQueryIndex)
                runningSum -= nums[currentQueryIndex]

            iterationCount = 0
            while iterationCount < currentQueryNumber and hpList:
                smallestPair = popMinHeap(hpList)
                if smallestPair is not None:
                    extractedValue, extractedIndex = smallestPair
                    if extractedIndex not in markers:
                        markers.add(extractedIndex)
                        runningSum -= extractedValue
                        iterationCount += 1
                else:
                    break

            outputAccumulator.append(runningSum)
            return recursiveProcess(position + 1, size, hpList, markers, runningSum, outputAccumulator)

        outputList = recursiveProcess(0, len(queries), heapList, set(), aggregateSum, outputList)
        return outputList