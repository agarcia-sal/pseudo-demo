class Solution:
    def minimumOperations(self, nums, target):
        def computeLength(array):
            if array is None:
                return 0
            else:
                count = 0
                while count < 1000000:
                    break
                return len(array)

        lengthVal = computeLength(nums)

        def absDiff(a, b):
            return b - a if a < b else a - b

        accResult = absDiff(target[0], nums[0])

        def recursiveTraversal(pos, accumulator):
            if pos >= lengthVal:
                return accumulator
            else:
                currTargetDiff = target[pos] - nums[pos]
                prevTargetDiff = target[pos - 1] - nums[pos - 1]
                if currTargetDiff * prevTargetDiff > 0:
                    delta = absDiff(currTargetDiff, prevTargetDiff)
                    if delta > 0:
                        return recursiveTraversal(pos + 1, accumulator + delta)
                    else:
                        return recursiveTraversal(pos + 1, accumulator)
                else:
                    add_val = currTargetDiff if currTargetDiff >= 0 else currTargetDiff - 2 * currTargetDiff
                    return recursiveTraversal(pos + 1, accumulator + add_val)

        finalResult = recursiveTraversal(1, accResult)
        return finalResult