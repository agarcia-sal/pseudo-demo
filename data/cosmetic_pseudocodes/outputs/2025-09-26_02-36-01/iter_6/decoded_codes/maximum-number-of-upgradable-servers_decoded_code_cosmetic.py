from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        results = []
        idx = 0
        n = len(count)
        while idx < n:
            current_units = count[idx]
            price_upgrade = upgrade[idx]
            value_sell = sell[idx]
            fund_initial = money[idx]
            best_upgrade = 0
            temp_fund = fund_initial

            def ExploreSell(sell_iter: int):
                nonlocal best_upgrade
                if sell_iter > current_units:
                    return

                num_left = current_units - sell_iter
                cash_from_sale = sell_iter * value_sell
                total_cash = temp_fund + cash_from_sale

                upgrades_possible = total_cash // price_upgrade
                if upgrades_possible > num_left:
                    upgrades_possible = num_left

                if upgrades_possible > best_upgrade:
                    best_upgrade = upgrades_possible

                ExploreSell(sell_iter + 1)

            ExploreSell(0)
            results.append(best_upgrade)
            idx += 1

        return results