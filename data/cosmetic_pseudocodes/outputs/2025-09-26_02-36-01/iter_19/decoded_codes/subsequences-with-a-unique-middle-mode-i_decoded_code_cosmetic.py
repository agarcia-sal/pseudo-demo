class Solution:
    def subsequencesWithMiddleMode(self, nums):
        M = 10**9 + 7
        xq = len(nums)
        if xq < 5:
            return 0
        ps = []

        def generate_combos(arr, combo, start, k):
            if k == 0:
                ps.append(combo)
                return
            w = start
            while w <= xq - k:
                generate_combos(arr, combo + [arr[w]], w + 1, k - 1)
                w += 1

        generate_combos(nums, [], 0, 5)
        oj = 0
        for vl in ps:
            tk = {}
            for ch in vl:
                tk[ch] = tk.get(ch, 0) + 1
            gy = vl[2]
            sc = tk[gy]
            ox = True
            zr = 0
            keys_list = list(tk.keys())
            vals_list = list(tk.values())
            while zr < len(keys_list):
                key = keys_list[zr]
                val = vals_list[zr]
                if key != gy and val >= sc:
                    ox = False
                    break
                zr += 1
            if ox:
                oj += 1
        return oj % M