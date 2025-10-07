from collections import Counter

class Solution:
    def maximumLength(self, nums):
        freq = Counter(nums)
        memo = {}

        def recur(z):
            if z not in freq or freq[z] < 2:
                if z in freq and freq[z] >= 1:
                    return 1
                else:
                    return 0
            if z in memo:
                return memo[z]
            squared = z * z
            computed = recur(squared) + 2
            memo[z] = computed
            return computed

        result = 1
        idx_list = list(freq.keys())
        pos = 1
        while pos <= len(idx_list):
            key = idx_list[pos - 1]
            if key == 1:
                c = freq[key]
                adjusted = c - 1 - ((c % 2) * 2)
                candidate = adjusted
                if candidate > result:
                    result = candidate
            else:
                candidate_2 = recur(key)
                if candidate_2 > result:
                    result = candidate_2
            pos += 1

        return result