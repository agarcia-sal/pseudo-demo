from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []
        outer_index = 0
        length = len(count)
        while outer_index < length:
            alpha = count[outer_index]
            beta = upgrade[outer_index]
            gamma = sell[outer_index]
            delta = money[outer_index]
            omega = 0
            sigma = delta
            inner_index = 0
            while inner_index <= alpha:
                rho = alpha - inner_index
                tau = inner_index * gamma
                phi = sigma + tau
                chi = phi // beta
                if chi > rho:
                    chi = rho
                if omega < chi:
                    omega = chi
                inner_index += 1
            result.append(omega)
            outer_index += 1
        return result