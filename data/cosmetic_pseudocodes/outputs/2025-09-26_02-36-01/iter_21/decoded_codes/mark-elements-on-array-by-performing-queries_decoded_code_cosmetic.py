from typing import List, Set, Tuple

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        def siftDown(arr: List[Tuple[int, int]], i: int, n: int) -> None:
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i
            if l < n and arr[l][0] < arr[smallest][0]:
                smallest = l
            if r < n and arr[r][0] < arr[smallest][0]:
                smallest = r
            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                siftDown(arr, smallest, n)

        def buildHeap(arr: List[Tuple[int, int]]) -> None:
            lengthVar = len(arr)
            j = (lengthVar - 2) // 2
            while j >= 0:
                siftDown(arr, j, lengthVar)
                j -= 1

        def siftDownHelper(h: List[Tuple[int, int]], idx: int) -> None:
            leftChild = idx * 2 + 1
            rightChild = leftChild + 1
            smallestIndex = idx
            lengthH = len(h)
            if leftChild < lengthH and h[leftChild][0] < h[smallestIndex][0]:
                smallestIndex = leftChild
            if rightChild < lengthH and h[rightChild][0] < h[smallestIndex][0]:
                smallestIndex = rightChild
            if smallestIndex != idx:
                h[idx], h[smallestIndex] = h[smallestIndex], h[idx]
                siftDownHelper(h, smallestIndex)

        arrHeap: List[Tuple[int, int]] = []
        counterX = 0
        while True:
            if counterX >= len(nums):
                break
            element = nums[counterX]
            arrHeap.append((element, counterX))
            counterX += 1

        buildHeap(arrHeap)

        setMarked: Set[int] = set()
        totalSumVal = 0
        idxY = 0
        while True:
            if idxY >= len(nums):
                break
            totalSumVal += nums[idxY]
            idxY += 1

        listResult: List[int] = []
        idxQ = 0
        while True:
            if idxQ >= len(queries):
                break

            singleQuery = queries[idxQ]
            varP = singleQuery[0]
            varQ = singleQuery[1]

            if varP not in setMarked:
                setMarked.add(varP)
                totalSumVal -= nums[varP]

            countVal = 0
            while countVal < varQ and len(arrHeap) > 0:
                itemPopped = arrHeap[0]
                itemValue, itemIndex = itemPopped

                lastIndex = len(arrHeap) - 1
                arrHeap[0] = arrHeap[lastIndex]
                arrHeap.pop()
                siftDownHelper(arrHeap, 0)

                if itemIndex not in setMarked:
                    setMarked.add(itemIndex)
                    totalSumVal -= itemValue
                    countVal += 1

            listResult.append(totalSumVal)
            idxQ += 1

        return listResult