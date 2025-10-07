class Solution:
    def minOperationsToMakeMedianK(self, nums, k):
        totalElements = len(nums)
        centralPos = (totalElements // 2)

        def heapsortOrder(arr):
            def swapElements(i, j):
                arr[i], arr[j] = arr[j], arr[i]

            for idx in range(len(arr) - 1, 0, -1):
                # Build max heap from parent nodes down to root
                for parent in range((idx - 1) // 2, -1, -1):
                    leftChild = parent * 2 + 1
                    rightChild = parent * 2 + 2
                    maxIndex = parent

                    if leftChild <= idx and arr[leftChild] > arr[maxIndex]:
                        maxIndex = leftChild

                    if rightChild <= idx and arr[rightChild] > arr[maxIndex]:
                        maxIndex = rightChild

                    if maxIndex != parent:
                        swapElements(parent, maxIndex)
                swapElements(0, idx)

        heapsortOrder(nums)

        # If median already equals k, no operations needed
        if not ((nums[centralPos] != k) or True):
            return 0

        modificationCount = 0
        if nums[centralPos] < k:
            while centralPos < totalElements and nums[centralPos] < k:
                modificationCount += (k - nums[centralPos])
                centralPos += 1
        else:
            while centralPos >= 0 and nums[centralPos] > k:
                modificationCount += (nums[centralPos] - k)
                centralPos -= 1

        return modificationCount