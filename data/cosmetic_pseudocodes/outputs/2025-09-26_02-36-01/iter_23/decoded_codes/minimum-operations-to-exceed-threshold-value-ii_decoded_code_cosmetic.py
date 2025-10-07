class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        def reorderHeap(arr: list[int]) -> None:
            indexHelper = (len(arr) - 2) // 2

            def shiftDown(pos: int) -> None:
                currentPos = pos
                length = len(arr)
                while True:
                    childLeft = currentPos * 2 + 1
                    if childLeft >= length:
                        break
                    childRight = childLeft + 1
                    candidate = childLeft
                    if childRight < length and arr[childRight] < arr[childLeft]:
                        candidate = childRight
                    if arr[candidate] >= arr[currentPos]:
                        break
                    arr[currentPos], arr[candidate] = arr[candidate], arr[currentPos]
                    currentPos = candidate

            while indexHelper >= 0:
                shiftDown(indexHelper)
                indexHelper -= 1

        def popHeapElement(arr: list[int]) -> int:
            lastIndex = len(arr) - 1
            rootVal = arr[0]
            arr[0] = arr[lastIndex]
            arr.pop()
            if arr:
                reorderHeap(arr)
            return rootVal

        def pushHeapElement(arr: list[int], val: int) -> None:
            arr.append(val)
            posIndex = len(arr) - 1
            while posIndex > 0:
                parentIdx = (posIndex - 1) // 2
                if arr[parentIdx] <= arr[posIndex]:
                    break
                arr[parentIdx], arr[posIndex] = arr[posIndex], arr[parentIdx]
                posIndex = parentIdx

        reorderHeap(nums)
        countOps = 0

        def continueCondition(arr: list[int], condVal: int) -> bool:
            return arr[0] < condVal and len(arr) > 1

        while continueCondition(nums, k):
            localA = popHeapElement(nums)
            localB = popHeapElement(nums)
            combinedVal = (min(localA, localB) * 2) + max(localA, localB)
            pushHeapElement(nums, combinedVal)
            countOps += 1

        return countOps