from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def tally_subsets(limit: int) -> int:
            totalSum = 0
            upperBound = 1 << n  # 2^n
            for mask in range(1, upperBound):
                combinedMultiple = 1
                setCount = 0
                for index in range(n):
                    if mask & (1 << index):
                        # Calculate lcm of combinedMultiple and coins[index]
                        g = gcd(combinedMultiple, coins[index])
                        combinedMultiple = combinedMultiple // g * coins[index]
                        setCount += 1
                        if combinedMultiple > limit:
                            # No need to continue if combinedMultiple exceeds limit
                            break
                else:
                    # Only add/subtract if combinedMultiple <= limit to avoid division by large number
                    if setCount % 2 == 1:
                        totalSum += limit // combinedMultiple
                    else:
                        totalSum -= limit // combinedMultiple
                    continue
                # If we broke out due to combinedMultiple > limit, no addition/subtraction needed
            return totalSum

        lowBound = 1
        upperBound = k * min(coins)
        while lowBound < upperBound:
            median = (lowBound + upperBound) // 2
            if tally_subsets(median) < k:
                lowBound = median + 1
            else:
                upperBound = median
        return lowBound