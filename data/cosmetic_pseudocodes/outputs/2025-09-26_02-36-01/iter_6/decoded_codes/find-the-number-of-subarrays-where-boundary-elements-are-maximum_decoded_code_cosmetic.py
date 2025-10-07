class Solution:
    def numberOfSubarrays(self, nums):
        def accumulateIndices(seq, pos, mapping):
            if pos >= len(seq):
                return mapping
            currVal = seq[pos]
            if currVal not in mapping:
                mapping[currVal] = []
            mapping[currVal].append(pos)
            return accumulateIndices(seq, pos + 1, mapping)

        index_map = accumulateIndices(nums, 0, {})

        def maxOf(arr, start, end):
            def recurMax(idx, currentMax):
                if idx > end:
                    return currentMax
                candidate = arr[idx]
                return recurMax(idx + 1, candidate if candidate > currentMax else currentMax)
            return recurMax(start, arr[start])

        totalCount = 0

        def processIndicesLists(lists, pos):
            nonlocal totalCount
            if pos >= len(lists):
                return
            currentList = lists[pos]
            sizeE = len(currentList)

            def outerLoop(i):
                if i > sizeE - 1:
                    return

                def innerLoop(j):
                    if j > sizeE - 1:
                        return
                    startIdx = currentList[i]
                    endIdx = currentList[j]
                    subNumStart = nums[startIdx]
                    maxVal = maxOf(nums, startIdx, endIdx)
                    if maxVal == subNumStart:
                        totalCount += 1
                    innerLoop(j + 1)

                innerLoop(i)
                outerLoop(i + 1)

            outerLoop(0)
            processIndicesLists(lists, pos + 1)

        idxLists = []
        for key in index_map:
            idxLists.insert(0, index_map[key])

        processIndicesLists(idxLists, 0)

        return totalCount