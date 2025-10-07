class Solution:
    def unmarkedSumArray(self, nums, queries):
        def heapifyLocal(arr):
            n = len(arr)

            def siftDownLocal(root):
                newRoot = root
                leftChild = (root << 1) + 1
                rightChild = (root << 1) + 2
                if leftChild < n and (arr[leftChild][0] < arr[newRoot][0] or
                                      (arr[leftChild][0] == arr[newRoot][0] and arr[leftChild][1] < arr[newRoot][1])):
                    newRoot = leftChild
                if rightChild < n and (arr[rightChild][0] < arr[newRoot][0] or
                                       (arr[rightChild][0] == arr[newRoot][0] and arr[rightChild][1] < arr[newRoot][1])):
                    newRoot = rightChild
                if newRoot != root:
                    arr[root], arr[newRoot] = arr[newRoot], arr[root]
                    siftDownLocal(newRoot)

            i = (n - 1) >> 1
            while i >= 0:
                siftDownLocal(i)
                i -= 1

        def heappopLocal(arr):
            poppedVal = arr[0]
            lastVal = arr[-1]
            arr.pop()
            if arr:
                arr[0] = lastVal
                heapifyLocal(arr)
            return poppedVal

        storeSet = set()
        trackedSum = 0
        idxValHeap = []

        posIter = 0
        lenNums = len(nums)
        while True:
            if posIter >= lenNums:
                break
            valCurr = nums[posIter]
            idxValHeap.append([valCurr, posIter])
            trackedSum += valCurr
            posIter += 1

        heapifyLocal(idxValHeap)

        ansList = []
        lenQueries = len(queries)

        def processQueries(qi, outputAcc):
            if qi >= lenQueries:
                return outputAcc

            idxQ, kQ = queries[qi]

            if idxQ not in storeSet:
                storeSet.add(idxQ)
                trackedSum_nonlocal[0] -= nums[idxQ]

            def popAndMark(countUsed):
                if countUsed < kQ and idxValHeap:
                    valP, idxP = heappopLocal(idxValHeap)
                    if idxP not in storeSet:
                        storeSet.add(idxP)
                        trackedSum_nonlocal[0] -= valP
                        popAndMark(countUsed + 1)
                    else:
                        popAndMark(countUsed)

            # Use a list to allow trackedSum updates in nested scope
            trackedSum_nonlocal = [trackedSum]
            popAndMark(0)
            trackedSum = trackedSum_nonlocal[0]

            outputAcc.append(trackedSum)
            return processQueries(qi + 1, outputAcc)

        return processQueries(0, ansList)