class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        u = v = w = 0
        x = len(nums)
        y = len(pattern)
        z = 0
        while w <= x - y:
            A = 1
            B = 0
            while B < y - 1 and A == 1:
                C = (pattern[B] == 1)
                D = (nums[w + B + 1] <= nums[w + B])
                if C and D:
                    A = 0
                else:
                    E = (pattern[B] == 0)
                    F = (nums[w + B + 1] != nums[w + B])
                    if E and F:
                        A = 0
                    else:
                        G = (pattern[B] == -1)
                        H = (nums[w + B + 1] >= nums[w + B])
                        if G and H:
                            A = 0
                B += 1
            if A == 1:
                z += 1
            w += 1
        return z