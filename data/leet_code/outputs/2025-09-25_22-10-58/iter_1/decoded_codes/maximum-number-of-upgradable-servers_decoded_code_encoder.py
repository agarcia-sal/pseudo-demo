from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        answer = []
        for i in range(len(count)):
            num_servers = count[i]
            upgrade_cost = upgrade[i]
            sell_price = sell[i]
            initial_money = money[i]

            max_upgrades = 0
            remaining_money = initial_money

            for sell_count in range(num_servers + 1):
                remaining_servers = num_servers - sell_count
                money_from_selling = sell_count * sell_price
                total_money = remaining_money + money_from_selling
                possible_upgrades = total_money // upgrade_cost
                if possible_upgrades > remaining_servers:
                    possible_upgrades = remaining_servers
                if possible_upgrades > max_upgrades:
                    max_upgrades = possible_upgrades

            answer.append(max_upgrades)
        return answer