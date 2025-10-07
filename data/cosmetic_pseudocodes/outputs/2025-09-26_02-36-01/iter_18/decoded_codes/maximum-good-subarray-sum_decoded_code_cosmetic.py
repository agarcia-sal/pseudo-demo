class Solution:
    def maximumSubarraySum(self, nums, k):
        dxr = dict()
        pwy = float('-inf')
        uzm = 0

        idx = 0
        while idx < len(nums):
            vxx = nums[idx]

            if (vxx - k) in dxr:
                qvm = uzm - dxr[vxx - k] + vxx
                if qvm > pwy:
                    pwy = qvm

            if (vxx + k) in dxr:
                jrm = uzm - dxr[vxx + k] + vxx
                if jrm > pwy:
                    pwy = jrm

            if vxx in dxr:
                if uzm < dxr[vxx]:
                    dxr[vxx] = uzm
            else:
                dxr[vxx] = uzm

            uzm += vxx
            idx += 1

        if pwy != float('-inf'):
            return pwy
        return 0