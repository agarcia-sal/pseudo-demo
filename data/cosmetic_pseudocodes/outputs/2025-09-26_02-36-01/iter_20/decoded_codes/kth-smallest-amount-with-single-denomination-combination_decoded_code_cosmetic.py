class Solution:
    def findKthSmallest(self, coins, k):
        def internal_counter(alpha):
            def gcf(a, b):
                u, v = a, b
                while v != 0:
                    w = u % v
                    u = v
                    v = w
                return u

            tally = 0
            upper_bound = (1 << len(coins)) - 1
            idx_outer = 1
            while idx_outer <= upper_bound:
                aggregate_lcm = 1
                set_cardinality = 0
                idx_inner = 0
                while idx_inner < len(coins):
                    if (idx_outer & (1 << idx_inner)) != 0:
                        prev_lcm = aggregate_lcm
                        divisor_element = coins[idx_inner]
                        div_gcd = gcf(prev_lcm, divisor_element)
                        aggregate_lcm = (prev_lcm * divisor_element) // div_gcd
                        set_cardinality += 1
                    idx_inner += 1
                if set_cardinality % 2 == 1:
                    quotient = alpha // aggregate_lcm
                    tally += quotient
                else:
                    quotient = alpha // aggregate_lcm
                    tally -= quotient
                idx_outer += 1
            return tally

        low = 1
        high = k * coins[0]
        while low < high:
            mid_val = (low + high) // 2
            comp_res = internal_counter(mid_val)
            if comp_res < k:
                low = mid_val + 1
            else:
                high = mid_val
        return low