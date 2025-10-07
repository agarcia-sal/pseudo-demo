from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []
        for i in range(len(count)):
            j83x = count[i]
            v12m = upgrade[i]
            q9ln = sell[i]
            c57b = money[i]
            max_upgrades = 0
            w8ks = c57b
            for dyt0 in range(j83x + 1):
                fzp3 = j83x - dyt0
                zmv6 = dyt0 * q9ln
                o7tr = w8ks + zmv6
                kx1n = o7tr // v12m  # integer division since upgrades must be whole
                if kx1n > fzp3:
                    kx1n = fzp3
                if kx1n > max_upgrades:
                    max_upgrades = kx1n
            result.append(max_upgrades)
        return result