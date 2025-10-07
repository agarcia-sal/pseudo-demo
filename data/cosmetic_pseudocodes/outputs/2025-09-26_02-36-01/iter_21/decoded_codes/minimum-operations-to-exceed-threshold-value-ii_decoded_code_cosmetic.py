class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        def buildHeap(arr: list[int]) -> None:
            p = len(arr) // 2
            while p >= 0:
                siftDown(arr, p, len(arr))
                p -= 1

        def siftDown(heapArr: list[int], startIndex: int, heapSize: int) -> None:
            root = startIndex
            while True:
                child = (root * 2) + 1
                if child >= heapSize:
                    break
                if child + 1 < heapSize and heapArr[child + 1] < heapArr[child]:
                    child += 1
                if heapArr[root] > heapArr[child]:
                    heapArr[root], heapArr[child] = heapArr[child], heapArr[root]
                    root = child
                else:
                    break

        def popHeap(heapList: list[int]) -> int:
            smallest = heapList[0]
            endIndex = len(heapList) - 1
            heapList[0] = heapList[endIndex]
            heapList.pop()
            if heapList:
                siftDown(heapList, 0, len(heapList))
            return smallest

        def pushHeap(heapList: list[int], value: int) -> None:
            heapList.append(value)
            idx = len(heapList) - 1
            while idx > 0:
                parentIdx = (idx - 1) // 2
                if heapList[parentIdx] > heapList[idx]:
                    heapList[parentIdx], heapList[idx] = heapList[idx], heapList[parentIdx]
                    idx = parentIdx
                else:
                    break

        buildHeap(nums)
        opCount = 0

        while nums and nums[0] < k:
            if len(nums) <= 1:
                break
            firstVal = popHeap(nums)
            secondVal = popHeap(nums)

            doubleMin, maxVal = (firstVal, secondVal)
            if secondVal < firstVal:
                doubleMin, maxVal = secondVal, firstVal

            combined = doubleMin + doubleMin + maxVal
            pushHeap(nums, combined)

            opCount += 1

        return opCount