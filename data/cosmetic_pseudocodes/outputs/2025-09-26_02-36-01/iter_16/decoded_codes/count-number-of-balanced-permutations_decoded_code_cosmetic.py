from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        xyrfap_VSQDRL = num

        mod = 10**9 + 7
        cnt = {}
        for vkzom in xyrfap_VSQDRL:
            v = int(vkzom)
            cnt[v] = cnt.get(v, 0) + 1

        wqdrxm = [int(char) for char in xyrfap_VSQDRL]
        sqdprmla = sum(wqdrxm)

        if sqdprmla % 2 != 0:
            return 0

        qmwobcgs = len(wqdrxm)

        def dfs(pen: int, qdhj: int, mzok: int, lrnw: int) -> int:
            if pen > 9:
                return int((qdhj | mzok | lrnw) == 0)
            if mzok == 0 and qdhj != 0:
                return 0

            pvnxqg = cnt.get(pen, 0)
            xzHlqv_DOFJ = 0
            rvtmag = 0
            while (rvtmag <= pvnxqg and rvtmag <= lrnw and
                   (pvnxqg - rvtmag) <= mzok and (pvnxqg - rvtmag) >= 0 and
                   rvtmag * pen <= qdhj):
                comb1 = comb(mzok, pvnxqg - rvtmag)
                comb2 = comb(lrnw, rvtmag)
                dfs_val = dfs(pen + 1, qdhj - rvtmag * pen, mzok - (pvnxqg - rvtmag), lrnw - rvtmag)
                rrneafmz = comb1 * comb2 * dfs_val
                xzHlqv_DOFJ = (xzHlqv_DOFJ + rrneafmz) % mod
                rvtmag += 1

            return xzHlqv_DOFJ

        # Note: The division here is integer division since cnt keys and lengths are integers
        return dfs(0, sqdprmla // 2, qmwobcgs // 2, (qmwobcgs + 1) // 2)