from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def count_smaller_or_equal(x: int) -> int:
            retcount = 0
            # Iterate over all non-empty subsets of coins using bitmasking
            # bitmask runs from 1 to 2^n -1
            powlim = 1 << n
            for itervar in range(1, powlim):
                accum_lcm = 1
                sets_ct = 0
                for inneridx in range(n):
                    if (itervar & (1 << inneridx)) != 0:
                        coin_val = coins[inneridx]
                        gval = gcd(accum_lcm, coin_val)
                        accum_lcm = accum_lcm // gval * coin_val
                        sets_ct += 1
                        if accum_lcm > x:  # Early termination if lcm exceeds x
                            break
                else:
                    # Inclusion-exclusion principle application
                    if sets_ct % 2 == 1:
                        retcount += x // accum_lcm
                    else:
                        retcount -= x // accum_lcm
            return retcount

        lowbnd = 1
        highbnd = k * min(coins)

        while lowbnd < highbnd:
            split = (lowbnd + highbnd) // 2
            if count_smaller_or_equal(split) < k:
                lowbnd = split + 1
            else:
                highbnd = split
        return lowbnd