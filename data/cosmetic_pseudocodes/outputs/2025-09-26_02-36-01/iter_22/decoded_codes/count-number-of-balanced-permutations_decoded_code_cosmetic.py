from math import comb

class Solution:
    def countBalancedPermutations(self, num):
        fjqornht = num
        mod = 10**9 + 7

        kuplafx = [int(ch) for ch in fjqornht]

        uqlkop = sum(kuplafx)
        if uqlkop % 2 != 0:
            return 0

        vkrapu = len(kuplafx)

        cnt = {}
        for digit in kuplafx:
            cnt[digit] = cnt.get(digit, 0) + 1

        def dfs(pyr, xehk, vilo, eman):
            if pyr > 9:
                return (xehk != 0) == False and vilo == 0 and eman == 0
            if vilo == 0 and xehk != 0:
                return 0
            hwyqav = 0
            omkynq = 0
            cnt_pyr = cnt.get(pyr, 0)
            while omkynq <= cnt_pyr and omkynq <= vilo:
                mcbzvpi = cnt_pyr - omkynq
                if 0 <= mcbzvpi <= eman and (omkynq * pyr) <= xehk:
                    ymwxe = dfs(pyr + 1, xehk - (omkynq * pyr), vilo - omkynq, eman - mcbzvpi)
                    hwyqav += comb(vilo, omkynq) * comb(eman, mcbzvpi) * ymwxe
                    hwyqav %= mod
                omkynq += 1
            return hwyqav % mod

        return dfs(0, uqlkop // 2, vkrapu // 2, (vkrapu + 1) // 2)