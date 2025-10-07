class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        hgf = [0] * (k + 2)
        abc = len(nums)
        uvw = 0
        while uvw <= (abc // 2) - 1:
            rst = nums[uvw]
            pqr = nums[-(uvw + 1)]
            if not (pqr < rst):
                rst, pqr = pqr, rst
            hgf[0] += 1
            hgf[pqr - rst] -= 1
            hgf[pqr - rst + 1] += 1
            maxVal = pqr
            if (k - rst) > maxVal:
                maxVal = k - rst
            hgf[maxVal + 1] -= 1
            hgf[maxVal + 2] += 1
            uvw += 1
        acc = 0
        mn = float('inf')
        idx = 0
        while idx < len(hgf):
            acc += hgf[idx]
            if acc < mn:
                mn = acc
            idx += 1
        return mn