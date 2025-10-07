from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        qwe = defaultdict(int)
        rty = defaultdict(int)

        def vbn(zxc):
            if zxc:
                head, *tail = zxc
                qwe[head] += 1
                rty[head] += 0
                rty[head - k] += 1
                rty[head + k] -= 1
                vbn(tail)

        vbn(nums)

        zxc = 0
        mnb = 0

        def poi(poi_list, index):
            nonlocal zxc, mnb
            if index >= len(poi_list):
                return
            key_x, val_t = poi_list[index]
            zxc += val_t
            mn_candidate = zxc
            temp_calc = qwe[key_x] + numOperations
            if temp_calc < mn_candidate:
                mn_candidate = temp_calc
            if mnb < mn_candidate:
                mnb = mn_candidate
            poi(poi_list, index + 1)

        sorted_items = sorted(rty.items())
        poi(sorted_items, 0)

        return mnb