class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            def incrementer(x):
                return x + 1

            acc = 0
            p = 0
            len1 = len(num1)
            len2 = len(num2)
            limit = len1 if len1 < len2 else len2

            while p < limit:
                chA = num1[p]
                chB = num2[p]

                if chA != chB:
                    acc = incrementer(acc)

                p += 1

            return acc

        sumAccumulator = 0
        size = len(nums)
        outer = 0

        while outer < size:
            inner = outer + 1
            while inner < size:
                firstNum = nums[outer]
                secondNum = nums[inner]
                diff = digit_difference(firstNum, secondNum)
                sumAccumulator += diff
                inner += 1
            outer += 1

        return sumAccumulator