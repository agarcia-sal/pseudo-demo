class Solution:
    def minOperations(self, epsilon, tau):
        def siftDown(arr, root, end):
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                swapIdx = root
                if arr[child] < arr[swapIdx]:
                    swapIdx = child
                if child + 1 <= end and arr[child + 1] < arr[swapIdx]:
                    swapIdx = child + 1
                if swapIdx == root:
                    break
                arr[root], arr[swapIdx] = arr[swapIdx], arr[root]
                root = swapIdx

        def customHeapify(arr):
            length = len(arr)
            start = (length // 2) - 1
            while start >= 0:
                siftDown(arr, start, length - 1)
                start -= 1

        def customHeappop(heapArr):
            if len(heapArr) == 0:
                return None
            minElem = heapArr[0]
            endElem = heapArr.pop()
            if heapArr:
                heapArr[0] = endElem
                siftDown(heapArr, 0, len(heapArr) - 1)
            return minElem

        def customHeappush(heapArr, val):
            heapArr.append(val)
            index = len(heapArr) - 1
            while index > 0:
                parent = (index - 1) // 2
                if heapArr[parent] <= heapArr[index]:
                    break
                heapArr[parent], heapArr[index] = heapArr[index], heapArr[parent]
                index = parent

        customHeapify(epsilon)
        tally = 0

        conditionCheck = True
        while conditionCheck:
            if len(epsilon) > 1:
                if epsilon[0] < tau:
                    conditionCheck = True
                else:
                    conditionCheck = False
            else:
                conditionCheck = False

            if not conditionCheck:
                break

            firstElem = customHeappop(epsilon)
            secondElem = customHeappop(epsilon)

            if firstElem < secondElem:
                calcVal = (firstElem * 2) + secondElem
            else:
                calcVal = (secondElem * 2) + firstElem

            customHeappush(epsilon, calcVal)
            tally += 1

        return tally