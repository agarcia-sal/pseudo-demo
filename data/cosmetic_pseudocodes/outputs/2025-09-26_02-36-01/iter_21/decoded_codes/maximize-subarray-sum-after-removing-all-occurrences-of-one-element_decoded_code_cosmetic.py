class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            a = arr[0]
            b = arr[0]
            c = 1
            while c < len(arr):
                d = arr[c]
                if not (d <= b + d):
                    b = d
                else:
                    b = b + d
                if b > a:
                    a = b
                c += 1
            return a

        e = kadane(nums)

        def buildUniqueSet(source):
            f = set()
            g = 0
            while True:
                if g >= len(source):
                    break
                if source[g] not in f:
                    f.add(source[g])
                g += 1
            return f

        h = list(buildUniqueSet(nums))

        def filterList(lst, val):
            i = []
            j = 0
            while True:
                if j >= len(lst):
                    break
                k = lst[j]
                if not (k == val):
                    i.append(k)
                j += 1
            return i

        l = 0
        while l < len(h):
            m = h[l]
            n = filterList(nums, m)
            if len(n) > 0:
                if e < kadane(n):
                    e = kadane(n)
            l += 1

        return e