from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []
        position = 0
        while position < len(count):
            total_servers = count[position]
            cost_per_upgrade = upgrade[position]
            price_per_sell = sell[position]
            available_funds = money[position]

            best_upgrade_count = 0
            sale_counter = 0
            while sale_counter <= total_servers:
                servers_left = total_servers - sale_counter
                funds_after_sale = available_funds + (sale_counter * price_per_sell)
                upgrades_possible = funds_after_sale // cost_per_upgrade

                if upgrades_possible > servers_left:
                    upgrades_possible = servers_left

                if upgrades_possible > best_upgrade_count:
                    best_upgrade_count = upgrades_possible

                sale_counter += 1

            result.append(best_upgrade_count)
            position += 1

        return result