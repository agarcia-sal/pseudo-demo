from collections import Counter

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        full_count = Counter(s)
        max_length = -1
        n = len(s)

        for i in range(n):
            current_count = Counter()
            for j in range(i, n):
                current_count[s[j]] += 1
                is_self_contained = True
                for char in current_count:
                    if current_count[char] < full_count[char]:
                        is_self_contained = False
                        break
                if is_self_contained and len(current_count) < len(full_count):
                    max_length = max(max_length, j - i + 1)
        return max_length