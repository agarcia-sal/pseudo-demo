from collections import Counter

class Solution:
    def maximumTotalDamage(self, power):
        frequency_map = Counter(power)
        sorted_keys = sorted(frequency_map.keys())
        n = len(sorted_keys)
        dp_map = {}

        for m in range(n):
            current_key = sorted_keys[m]

            exclude_val = dp_map.get(sorted_keys[m - 1], 0) if m > 0 else 0

            include_val = current_key * frequency_map[current_key]

            l = m - 1
            while l >= 0:
                if sorted_keys[l] < current_key - 1:
                    break
                l -= 1

            if l >= 0:
                include_val += dp_map.get(sorted_keys[l], 0)

            dp_map[current_key] = max(include_val, exclude_val)

        max_damage = max(dp_map.values(), default=0)
        return max_damage