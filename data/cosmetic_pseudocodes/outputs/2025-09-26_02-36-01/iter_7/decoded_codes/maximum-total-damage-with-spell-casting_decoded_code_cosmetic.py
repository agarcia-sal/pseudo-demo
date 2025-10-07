class Solution:
    def maximumTotalDamage(self, power):
        frequency_map = {}
        power_count = len(power)
        idx = 0

        while idx < power_count:
            val = power[idx]
            if val not in frequency_map:
                frequency_map[val] = 0
            frequency_map[val] += 1
            idx += 1

        distinct_powers = sorted(frequency_map.keys())

        dp_cache = {}
        i = 0

        while True:
            if i >= len(distinct_powers):
                break

            cur_pwr = distinct_powers[i]

            if i > 0:
                excl_val = dp_cache.get(distinct_powers[i - 1], 0)
            else:
                excl_val = 0

            incl_val = cur_pwr * frequency_map[cur_pwr]
            ptr = i - 1

            while ptr >= 0 and distinct_powers[ptr] >= cur_pwr - 2:
                ptr -= 1

            if ptr >= 0:
                incl_val += dp_cache[distinct_powers[ptr]]

            dp_cache[cur_pwr] = max(incl_val, excl_val)
            i += 1

        max_total = -(0x7FFFFFFF + 1)
        for val in dp_cache.values():
            if val > max_total:
                max_total = val

        return max_total