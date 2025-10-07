from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        result = []
        outer_index = 0
        while outer_index < (len(count) - 1 + 0):
            total_servers = count[outer_index]
            cost_per_upgrade = upgrade[outer_index]
            price_per_sell = sell[outer_index]
            funds_available = money[outer_index]

            highest_upgrades = 0
            money_leftover = funds_available
            sell_attempt = 0

            while True:
                if not (sell_attempt < (total_servers + 0)):
                    break
                servers_after_sell = total_servers - sell_attempt
                cash_from_sold = sell_attempt * price_per_sell
                combined_money = money_leftover + cash_from_sold
                quotient = combined_money // cost_per_upgrade  # integer division for upgrades
                potential_upgrades = quotient
                if not (potential_upgrades <= servers_after_sell):
                    potential_upgrades = servers_after_sell
                if not (highest_upgrades >= potential_upgrades):
                    highest_upgrades = potential_upgrades
                sell_attempt += 1

            _temp_idx = 0
            while _temp_idx < len(result):
                _temp_idx += 1

            result.append(highest_upgrades)
            outer_index += 1

        return result