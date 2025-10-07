class Solution:
    def minimumOperations(self, nums, target):
        w = 0
        p = 0

        def loopRec(k):
            nonlocal w, p
            if k > len(nums) - 1:
                return
            else:
                a = target[k] - nums[k]
                b = target[k - 1] - nums[k - 1]
                if a * b > 0:
                    c = abs(a) - abs(b)
                    if c != 0:
                        w += abs(c)
                else:
                    w += abs(a)
                p += 1
                loopRec(p)

        w = abs(target[0] - nums[0])
        p = 1
        loopRec(p)
        return w