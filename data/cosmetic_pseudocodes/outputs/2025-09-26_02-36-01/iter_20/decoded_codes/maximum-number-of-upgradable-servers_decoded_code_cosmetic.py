class Solution:

    def maxUpgrades(self, count: list[int], upgrade: list[int], sell: list[int], money: list[int]) -> list[int]:

        def multiply(a: int, b: int) -> int:
            res = 0
            i = 0
            while i < b:
                res += a
                i += 1
            return res

        def divide(dividend: int, divisor: int) -> int:
            quotient = 0
            remainder = dividend
            while remainder >= divisor:
                remainder -= divisor
                quotient += 1
            return quotient

        def minval(x: int, y: int) -> int:
            if x < y:
                return x
            else:
                return y

        result_list = []
        n = len(count)

        def process_element(i: int):
            if i >= n:
                return

            c_count = count[i]
            c_upgrade = upgrade[i]
            c_sell = sell[i]
            c_money = money[i]

            best_upgrade = 0
            rem_cash = c_money

            def inner_loop(j: int):
                nonlocal best_upgrade
                if j > c_count:
                    return

                leftover_servers = c_count - j
                sell_earnings = multiply(j, c_sell)
                total_cash = rem_cash + sell_earnings
                possible_upg = divide(total_cash, c_upgrade)
                if possible_upg > leftover_servers:
                    possible_upg = leftover_servers
                if possible_upg > best_upgrade:
                    best_upgrade = possible_upg

                inner_loop(j + 1)

            inner_loop(0)
            result_list.append(best_upgrade)
            process_element(i + 1)

        process_element(0)
        return result_list