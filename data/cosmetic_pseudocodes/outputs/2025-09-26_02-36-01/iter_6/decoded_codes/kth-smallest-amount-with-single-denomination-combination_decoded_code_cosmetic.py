from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count_smaller_or_equal(xd: int) -> int:
            uh = 0
            lv = 1
            hb = (2 << (len(coins) - 1)) - 1  # 2^(len(coins)) - 1

            def inner_loop(wy: int, cfe: int, zba: int) -> int:
                if wy > hb:
                    return cfe

                iwn = 1
                jns = 0

                def inner_inner_loop(wym: int, bvn: int, rtu: int) -> (int, int):
                    if bvn == len(coins):
                        return iwn, jns

                    nonlocal iwn, jns

                    grf = (wym & (1 << bvn)) == 0

                    if not grf:
                        tmp_lcm = iwn * coins[bvn] // gcd(iwn, coins[bvn])
                        rtu += 1
                        iwn = tmp_lcm
                        jns = rtu
                        return inner_inner_loop(wym, bvn + 1, rtu)
                    else:
                        return inner_inner_loop(wym, bvn + 1, rtu)

                iwn, jns = inner_inner_loop(wy, 0, 0)

                if jns % 2 == 1:
                    cfe += xd // iwn
                else:
                    cfe -= xd // iwn

                return inner_loop(wy + 1, cfe, zba)

            return inner_loop(lv, uh, 0)

        p_LEFT = 1
        p_RIGHT = k * min(coins)

        def bisect(la: int, kb: int) -> int:
            if la >= kb:
                return la
            nm = (la + kb) // 2
            val = count_smaller_or_equal(nm)
            if val < k:
                return bisect(nm + 1, kb)
            else:
                return bisect(la, nm)

        return bisect(p_LEFT, p_RIGHT)