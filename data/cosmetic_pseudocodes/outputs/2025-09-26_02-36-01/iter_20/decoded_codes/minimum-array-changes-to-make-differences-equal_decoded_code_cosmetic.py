class Solution:
    def minChanges(self, nums, k):
        def customMax(a, b):
            return a if a > b else b

        def customLength(arr):
            count = 0
            while True:
                try:
                    _ = arr[count]
                    count += 1
                except:
                    break
            return count

        def customMin(arr):
            result = arr[0]
            idx = 1
            length = customLength(arr)
            while idx < length:
                if arr[idx] < result:
                    result = arr[idx]
                idx += 1
            return result

        z = k + 2
        o = 0
        d = []
        while True:
            d.append(0)
            o += 1
            if o == z:
                break

        r = customLength(nums)
        s = 0
        while s < (r // 2):
            p = nums[s]
            q = nums[(r - 1) - s]

            if p > q:
                p, q = q, p

            d[0] += 1
            pos1 = q - p
            d[pos1] -= 1
            pos2 = (q - p) + 1
            d[pos2] += 1
            maxVal = customMax(q, (k - p) + 1)
            d[maxVal] -= 1
            d[maxVal + 1] += 1

            s += 1

        total = 0
        idx = 0
        while idx < (k + 1):
            total += d[idx]
            d[idx] = total
            idx += 1

        return customMin(d)