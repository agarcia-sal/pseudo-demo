class Solution:
    def earliestSecondToMarkIndices(self, changeIndices):
        nums = changeIndices  # The pseudocode uses nums, but input is changeIndices only. Actually nums is external?

        # From pseudocode, nums and changeIndices are inputs, but only changeIndices is parameter here.
        # So nums must be defined outside or is it a global? That's ambiguous.
        #
        # On review, 'nums' is used as an input parameter in the function earliestSecondToMarkIndices,
        # but in the pseudocode, earliestSecondToMarkIndices takes a parameter "changeIndices" only.
        # But it uses "nums" inside helper - meaning nums is a closure or from outer scope,
        # but it's not passed explicitly.
        #
        # Seems like the pseudocode expects nums to be a global or captured variable; we need to preserve the function signature as is.
        #
        # So the only input is changeIndices.
        # But nums is never explicitly passed? The pseudocode does not clarify how nums is acquired.
        #
        # We'll assume nums is a member variable or a global variable accessible to the function.
        # To be safe, let's modify the function signature to accept nums as well.
        #
        # But the instructions say strictly preserve all class names, function names, and signatures exactly as specified.
        #
        # So we cannot add parameters.
        #
        # So considering that, maybe the function 'earliestSecondToMarkIndices' in the pseudocode is a method of Solution class,
        # and nums is a member variable of the class.
        #
        # To maintain fidelity, we can add an __init__ method that sets self.nums.
        #
        # The pseudocode is incomplete or ambiguous about how nums is given.
        #
        # Because of this, let's assume that changeIndices is a list of integers,
        # and nums is a list of integers defined as a property or passed externally before calling.
        #
        # We will add an __init__ to accept nums, and earliestSecondToMarkIndices will only accept changeIndices.
        #
        # This is consistent with the problem requirement to preserve all function and class signatures.
        #
        # So we will:
        # - add __init__(self, nums)
        # - store nums as an instance variable
        # - earliestSecondToMarkIndices(changeIndices) uses self.nums internally

    def __init__(self, nums):
        self.nums = nums

    def earliestSecondToMarkIndices(self, changeIndices):
        nums = self.nums

        def helper(k):
            arr = [-1] * len(nums)

            count2 = 0
            uniqueSet = set()

            pos = 0
            while pos < k:
                x = changeIndices[pos] - 1
                arr[x] = pos
                pos += 1

            # sumTotal unused in pseudocode's logic beyond calculating - confirmed ignoring.

            pos = 0
            while pos < k:
                y = changeIndices[pos] - 1
                if y not in uniqueSet:
                    if arr[y] == pos:
                        if nums[y] <= count2:
                            count2 -= nums[y]
                            uniqueSet.add(y)
                        else:
                            return False
                    else:
                        count2 += 1
                else:
                    count2 += 1
                pos += 1

            return len(uniqueSet) == len(nums)

        a = 0
        b = len(changeIndices) + 1

        while a < b:
            midVal = a + (b - a) // 2
            if helper(midVal):
                b = midVal
            else:
                a += 1

        return a if a <= len(changeIndices) else -1