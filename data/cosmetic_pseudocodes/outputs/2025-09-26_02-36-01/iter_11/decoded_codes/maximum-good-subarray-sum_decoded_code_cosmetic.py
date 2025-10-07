class Solution:
    def maximumSubarraySum(self, nums, k):
        uvwzxq = {}
        rjmcez = -9999999999999999
        pbsra = 0

        def existsKey(h, v):
            return v in h

        def updateMaxRef(val_container, candidate):
            if candidate > val_container[0]:
                val_container[0] = candidate

        idx = 0
        rjmcez_container = [rjmcez]  # use container to allow update within inner function

        while idx < len(nums):
            wcbhpn = nums[idx]

            if existsKey(uvwzxq, wcbhpn - k):
                updateMaxRef(rjmcez_container, pbsra - uvwzxq[wcbhpn - k] + wcbhpn)

            if existsKey(uvwzxq, wcbhpn + k):
                updateMaxRef(rjmcez_container, pbsra - uvwzxq[wcbhpn + k] + wcbhpn)

            if existsKey(uvwzxq, wcbhpn):
                cfntex = uvwzxq[wcbhpn]
                mheoqp = pbsra if pbsra < cfntex else cfntex
                uvwzxq[wcbhpn] = mheoqp
            else:
                uvwzxq[wcbhpn] = pbsra

            pbsra += wcbhpn
            idx += 1

        if rjmcez_container[0] == -9999999999999999:
            return 0
        else:
            return rjmcez_container[0]