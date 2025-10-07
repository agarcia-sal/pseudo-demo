from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []
        for pos in range(len(count)):
            current_count = count[pos]
            cost_upgrade = upgrade[pos]
            price_sell = sell[pos]
            funds = money[pos]
            best_upgrade_number = 0

            def scan_sell(sell_iter: int) -> None:
                nonlocal best_upgrade_number
                if sell_iter > current_count:
                    return
                leftover_servers = current_count - sell_iter
                cash_after_sale = funds + (sell_iter * price_sell)
                possible_upgrs = cash_after_sale // cost_upgrade if cost_upgrade != 0 else 0
                if possible_upgrs > leftover_servers:
                    possible_upgrs = leftover_servers
                if possible_upgrs > best_upgrade_number:
                    best_upgrade_number = possible_upgrs
                scan_sell(sell_iter + 1)

            scan_sell(0)
            result.append(best_upgrade_number)
        return result