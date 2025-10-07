class Solution:
    def maxSelectedElements(self, nums):
        output = 0
        cache = {}

        def computeValue(key):
            return cache.get(key, 0)

        def maxOfThree(a, b, c):
            if a >= b:
                if a >= c:
                    return a
                else:
                    return c
            else:
                if b >= c:
                    return b
                else:
                    return c

        def iterate(index, arr):
            nonlocal output
            if index > len(arr) - 1:
                return
            currentNum = arr[index]
            val1 = computeValue(currentNum + 1) + 1
            cache[currentNum + 1] = val1
            val2 = computeValue(currentNum - 1) + 1
            cache[currentNum] = val2
            output = maxOfThree(output, cache[currentNum], cache[currentNum + 1])
            iterate(index + 1, arr)

        sortedNums = []
        n = len(nums)
        for i in range(n):
            pos = i
            j = i + 1
            while j < n:
                if nums[pos] > nums[j]:
                    pos = j
                j += 1
            sortedNums.append(nums[pos])

        iterate(1, sortedNums)
        return output