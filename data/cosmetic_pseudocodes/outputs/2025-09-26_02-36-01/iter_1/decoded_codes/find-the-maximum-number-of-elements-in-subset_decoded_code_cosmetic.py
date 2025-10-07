from collections import Counter

class Solution:
    def maximumLength(self, nums):
        freq = Counter(nums)
        cache = {}

        def computeChainLength(value):
            if value not in freq or freq[value] < 2:
                if value in freq and freq[value] >= 1:
                    return 1
                return 0
            if value in cache:
                return cache[value]
            squared_value = value * value
            chain_length = computeChainLength(squared_value) + 2
            cache[value] = chain_length
            return chain_length

        longest = 1
        for element in freq:
            if element == 1:
                count = freq[element]
                adjusted_length = count - 1 - ((count % 2) * 2)
                longest = max(longest, adjusted_length)
            else:
                longest = max(longest, computeChainLength(element))

        return longest