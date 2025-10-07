class Solution:
    def maxUpgrades(
        self,
        count: list[int],
        upgrade: list[int],
        sell: list[int],
        money: list[int],
    ) -> list[int]:
        result = []
        i = 0
        while i < len(count):
            total_servers = count[i]
            price_to_upgrade = upgrade[i]
            price_to_sell = sell[i]
            available_funds = money[i]

            highest_possible_upgrades = 0
            sell_attempt = 0

            while sell_attempt <= total_servers:
                servers_left = total_servers - sell_attempt
                funds_after_sale = available_funds + sell_attempt * price_to_sell
                upgrades_affordable = funds_after_sale // price_to_upgrade

                if upgrades_affordable > servers_left:
                    upgrades_affordable = servers_left

                if upgrades_affordable > highest_possible_upgrades:
                    highest_possible_upgrades = upgrades_affordable

                sell_attempt += 1

            result.append(highest_possible_upgrades)
            i += 1

        return result