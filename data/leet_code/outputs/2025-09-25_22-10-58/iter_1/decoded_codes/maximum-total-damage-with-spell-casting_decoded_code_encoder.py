from collections import Counter

class Solution:
    def maximumTotalDamage(self, power):
        count = Counter(power)
        unique_powers = sorted(count.keys())
        dp = {}

        for index in range(len(unique_powers)):
            p = unique_powers[index]

            exclude = dp.get(unique_powers[index - 1], 0) if index > 0 else 0

            include = p * count[p]

            j = index - 1
            while j >= 0 and unique_powers[j] >= p - 2:
                j -= 1

            if j >= 0:
                include += dp[unique_powers[j]]

            dp[p] = max(include, exclude)

        return max(dp.values()) if dp else 0