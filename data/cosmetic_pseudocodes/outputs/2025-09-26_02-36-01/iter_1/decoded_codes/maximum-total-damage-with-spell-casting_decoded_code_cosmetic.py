class Solution:
    def maximumTotalDamage(self, power):
        frequency_map = {}
        for val in power:
            frequency_map[val] = frequency_map.get(val, 0) + 1

        sorted_powers = sorted(frequency_map.keys())
        memo = {}

        for idx in range(len(sorted_powers)):
            current_power = sorted_powers[idx]

            opt_exclude = memo[sorted_powers[idx - 1]] if idx > 0 and sorted_powers[idx - 1] in memo else 0
            opt_include = current_power * frequency_map[current_power]

            scan_idx = idx - 1
            while scan_idx >= 0 and sorted_powers[scan_idx] >= current_power - 2:
                scan_idx -= 1

            if scan_idx >= 0:
                opt_include += memo[sorted_powers[scan_idx]]

            memo[current_power] = max(opt_include, opt_exclude)

        return max(memo.values()) if memo else 0