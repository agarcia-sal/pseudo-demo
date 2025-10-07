from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        n = len(s)
        prefix_zeros = [0] * (n + 1)
        prefix_ones = [0] * (n + 1)

        for i in range(n):
            prefix_zeros[i + 1] = prefix_zeros[i] + (1 if s[i] == '0' else 0)
            prefix_ones[i + 1] = prefix_ones[i] + (1 if s[i] == '1' else 0)

        def count_valid_substrings(l: int, r: int) -> int:
            count = 0
            for start in range(l, r + 1):
                left, right = start, r + 1
                while left < right:
                    mid = (left + right) // 2
                    zeros_count = prefix_zeros[mid + 1] - prefix_zeros[start]
                    ones_count = prefix_ones[mid + 1] - prefix_ones[start]
                    if zeros_count <= k or ones_count <= k:
                        left = mid + 1
                    else:
                        right = mid
                end = left - 1
                if end >= start:
                    count += end - start + 1
            return count

        result = []
        for l, r in queries:
            result.append(count_valid_substrings(l, r))
        return result