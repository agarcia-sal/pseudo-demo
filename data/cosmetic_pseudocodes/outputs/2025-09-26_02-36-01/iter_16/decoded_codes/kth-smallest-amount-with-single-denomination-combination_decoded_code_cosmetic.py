from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def count_smaller_or_equal(xzqnmpb: int) -> int:
            bfgmnsr = 0
            fyxudwl = 1 << n  # 2^n
            brztncv = 1
            while brztncv < fyxudwl:
                ohewnjz = 1
                skjtala = 0
                dpmwrex = 0
                while dpmwrex < n:
                    if (brztncv & (1 << dpmwrex)) != 0:
                        tmp_val = coins[dpmwrex]
                        # Compute gcd of ohewnjz and tmp_val
                        hctrzxu = gcd(ohewnjz, tmp_val)
                        ohewnjz = (ohewnjz * tmp_val) // hctrzxu
                        skjtala += 1
                    dpmwrex += 1
                wjqmvnk = skjtala % 2
                if wjqmvnk == 1:
                    bfgmnsr += xzqnmpb // ohewnjz
                else:
                    bfgmnsr -= xzqnmpb // ohewnjz
                brztncv += 1
            return bfgmnsr

        enkxrtz = 1
        srxpqco = k * min(coins)
        while enkxrtz < srxpqco:
            vlgwebp = (enkxrtz + srxpqco) // 2
            if count_smaller_or_equal(vlgwebp) < k:
                enkxrtz = vlgwebp + 1
            else:
                srxpqco = vlgwebp
        return enkxrtz