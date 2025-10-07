class Solution:
    def minimumOperations(self, nums, target):
        size = len(nums)
        acc = abs(target[0] - nums[0])

        def absVal(num):
            return -num if num < 0 else num

        index = 1
        while index < size:
            valA = target[index] - nums[index]
            valB = target[index - 1] - nums[index - 1]

            def productPositive(a, b):
                return (a * b) > 0

            if productPositive(valA, valB):
                def diffAbs(a, b):
                    return absVal(a) - absVal(b)

                delta = absVal(diffAbs(valA, valB))
                if delta > 0:
                    acc += delta
            else:
                acc += absVal(valA)
            index += 1
        return acc