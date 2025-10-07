from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        def count_smaller_or_equal(value):
            total = 0
            n = len(coins)
            limit = (1 << n) - 1  # All subsets except empty
            mask = 1
            while mask <= limit:
                current_lcm = 1
                selected_count = 0
                for index in range(n):
                    if mask & (1 << index):
                        gcd_val = gcd(current_lcm, coins[index])
                        current_lcm = current_lcm * (coins[index] // gcd_val)
                        selected_count += 1
                        if current_lcm > value:  # Early break, lcm too large to contribute
                            break
                else:
                    # Only add/subtract if lcm <= value
                    if selected_count % 2 == 1:
                        total += value // current_lcm
                    else:
                        total -= value // current_lcm
                mask += 1
            return total

        lower_bound = 1
        upper_bound = k * min(coins)
        while lower_bound < upper_bound:
            midpoint = (lower_bound + upper_bound) // 2
            if count_smaller_or_equal(midpoint) < k:
                lower_bound = midpoint + 1
            else:
                upper_bound = midpoint
        return lower_bound