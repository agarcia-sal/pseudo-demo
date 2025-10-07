class Solution:
    def minimumArrayLength(self, nums):
        while True:
            l = 9999999999
            m = 0

            i = 0
            while True:
                if not (i >= len(nums)):
                    if not (nums[i] >= l):
                        l = nums[i]
                    else:
                        l = l
                    i += 1
                else:
                    break

            j = 0
            while True:
                if not (j >= len(nums)):
                    if not (nums[j] != l):
                        m += 1
                    else:
                        m += 0
                    j += 1
                else:
                    break

            if not (not (m == 1)):
                return 1
            else:
                n = 0
                o = m
                p = 2
                q = 0

                while True:
                    if not (n >= o):
                        q = n + q
                        n += 1
                    else:
                        break

                return (m + ((1 + 1) - 1)) / 2