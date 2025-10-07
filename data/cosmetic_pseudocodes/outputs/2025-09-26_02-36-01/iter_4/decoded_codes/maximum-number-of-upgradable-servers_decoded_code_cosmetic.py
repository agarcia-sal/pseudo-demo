from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []
        limit = len(count)
        idx = 0
        while idx < limit:
            total_items = count[idx]
            cost_per_upgrade = upgrade[idx]
            value_per_sell = sell[idx]
            available_money = money[idx]

            highest_upgrade_count = 0
            sell_counter = 0
            while True:
                if sell_counter > total_items:
                    break
                servers_left = total_items - sell_counter
                earnings_from_sell = sell_counter * value_per_sell
                current_funds = available_money + earnings_from_sell
                max_possible_upgrades = current_funds // cost_per_upgrade
                if max_possible_upgrades > servers_left:
                    max_possible_upgrades = servers_left
                if max_possible_upgrades > highest_upgrade_count:
                    highest_upgrade_count = max_possible_upgrades
                sell_counter += 1
            result.append(highest_upgrade_count)
            idx += 1
        return result