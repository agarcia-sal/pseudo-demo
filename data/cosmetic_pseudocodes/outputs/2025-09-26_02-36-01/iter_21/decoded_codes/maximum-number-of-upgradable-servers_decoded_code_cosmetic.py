from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        output = []
        idx = 0

        while idx < len(count):
            a = count[idx]
            b = upgrade[idx]
            c = sell[idx]
            d = money[idx]

            def computeMax(f: int, g: int, h: int, i: int) -> int:
                res = 0
                curr = i
                j = f
                while j >= 0:
                    k = j
                    l = h * k
                    m = curr + l
                    n = m // g
                    if n > f - k:
                        n = f - k
                    if res < n:
                        res = n
                    j -= 1
                return res

            result = computeMax(a, b, c, d)
            output.append(result)
            idx += 1

        return output