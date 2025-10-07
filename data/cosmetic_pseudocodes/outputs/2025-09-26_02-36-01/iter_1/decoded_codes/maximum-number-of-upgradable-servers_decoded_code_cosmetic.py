from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []
        for i in range(len(count)):
            total_servers = count[i]
            cost_upgrade = upgrade[i]
            price_sell = sell[i]
            budget = money[i]
            best_upgrade = -1
            for servers_sold in range(total_servers + 1):
                servers_left = total_servers - servers_sold
                funds_after_sale = budget + servers_sold * price_sell
                achievable_upgrades = funds_after_sale // cost_upgrade
                if achievable_upgrades > servers_left:
                    achievable_upgrades = servers_left
                if achievable_upgrades > best_upgrade:
                    best_upgrade = achievable_upgrades
            result.append(best_upgrade)
        return result