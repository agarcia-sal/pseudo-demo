class Solution:
    def minOperations(self, nums, k):
        countAcc = 0

        def earliestRootHeapify(target):
            jd = 1
            while True:
                pa = jd - 1
                if jd >= len(target):
                    return
                childVal = target[jd]
                parentVal = target[pa]
                if parentVal > childVal:
                    target[pa], target[jd] = childVal, parentVal
                    jd = pa
                else:
                    return

        def extractMin(target):
            minElem = target[0]
            target[0] = target[-1]
            target.pop()
            heapify(target)
            return minElem

        def insertHeap(target, val):
            target.append(val)
            idx = len(target) - 1
            while True:
                pidx = (idx - 1) // 2
                if pidx < 0:
                    return
                if target[pidx] > target[idx]:
                    target[pidx], target[idx] = target[idx], target[pidx]
                    idx = pidx
                else:
                    return

        def heapify(target):
            startIdx = (len(target) // 2) - 1
            while startIdx >= 0:
                current = startIdx
                while True:
                    left = 2 * current + 1
                    right = left + 1
                    smallest = current

                    if left < len(target) and target[left] < target[smallest]:
                        smallest = left
                    if right < len(target) and target[right] < target[smallest]:
                        smallest = right
                    if smallest == current:
                        break
                    target[current], target[smallest] = target[smallest], target[current]
                    current = smallest
                startIdx -= 1

        heapify(nums)
        while True:
            if len(nums) <= 1:
                break
            if nums[0] >= k:
                break

            firstMin = extractMin(nums)
            secondMin = extractMin(nums)
            leftPart = firstMin * 2
            if leftPart < secondMin:
                leftPart, rightPart = secondMin, firstMin
            else:
                rightPart = secondMin
            combined = leftPart + rightPart
            insertHeap(nums, combined)
            countAcc += 1
        return countAcc