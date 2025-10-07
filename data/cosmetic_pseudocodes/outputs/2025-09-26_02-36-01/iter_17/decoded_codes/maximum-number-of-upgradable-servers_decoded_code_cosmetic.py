from math import floor
from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []
        for i in range(len(count)):
            current_count = count[i]
            cost_upgrade = upgrade[i]
            price_sell = sell[i]
            budget = money[i]
            highest_upgrades = 0
            for inner_index in range(current_count + 1):
                remaining_servers = current_count - inner_index
                revenue = inner_index * price_sell
                funds = budget + revenue
                achievable_upgrades = floor(funds / cost_upgrade)
                if achievable_upgrades > remaining_servers:
                    achievable_upgrades = remaining_servers
                if highest_upgrades < achievable_upgrades:
                    highest_upgrades = achievable_upgrades
            result.append(highest_upgrades)
        return result