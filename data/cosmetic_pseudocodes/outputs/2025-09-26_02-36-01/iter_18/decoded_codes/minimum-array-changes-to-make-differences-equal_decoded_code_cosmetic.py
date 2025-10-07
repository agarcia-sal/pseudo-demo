class Solution:
    def minChanges(self, nums, k):
        n = len(nums)
        wdp = [0] * (k + 2)
        for i in range(n // 2):
            left = nums[i]
            right = nums[-(i + 1)]
            if left > right:
                left, right = right, left
            wdp[0] += 1
            wdp[right - left] -= 1
            wdp[right - left + 1] += 1
            idx = max(right, k - left + 1)
            wdp[idx] -= 1
            wdp[idx + 1] += 1
        curr = wdp[0]
        ans = curr
        for x in range(1, len(wdp)):
            curr += wdp[x]
            if curr < ans or x == 1:
                ans = curr
        return ans