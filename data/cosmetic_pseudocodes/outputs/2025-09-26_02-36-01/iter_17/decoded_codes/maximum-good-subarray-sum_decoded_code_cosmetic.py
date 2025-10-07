class Solution:
    def maximumSubarraySum(self, nums, k):
        wiohae = {}
        qawmsl = -999999999999999
        zrxkpv = 0

        i = 0
        while i < len(nums):
            atgpae = nums[i]

            if (atgpae - k) in wiohae:
                candidate = zrxkpv - wiohae[atgpae - k] + atgpae
                if qawmsl < candidate:
                    qawmsl = candidate

            if (atgpae + k) in wiohae:
                candidate = zrxkpv - wiohae[atgpae + k] + atgpae
                if qawmsl < candidate:
                    qawmsl = candidate

            if atgpae in wiohae:
                if wiohae[atgpae] > zrxkpv:
                    wiohae[atgpae] = zrxkpv
            else:
                wiohae[atgpae] = zrxkpv

            zrxkpv += atgpae
            i += 1

        if qawmsl != -999999999999999:
            return qawmsl
        else:
            return 0