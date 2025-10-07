from typing import List

class Solution:
    def maxUpgrades(
        self,
        count: List[int],
        upgrade: List[int],
        sell: List[int],
        money: List[int]
    ) -> List[int]:
        result = []
        pos = 0
        n = len(count)
        while pos < n:
            servers_qty = count[pos]
            cost_upgrade = upgrade[pos]
            price_sell = sell[pos]
            funds = money[pos]
            peak_upgrade = 0
            try_sell = servers_qty
            while try_sell >= 0:
                left_servers = servers_qty - try_sell
                cash_gain = try_sell * price_sell
                total_funds = funds + cash_gain
                possible = total_funds // cost_upgrade
                if possible > left_servers:
                    possible = left_servers
                if possible > peak_upgrade:
                    peak_upgrade = possible
                try_sell -= 1
            result.append(peak_upgrade)
            pos += 1
        return result