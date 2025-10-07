from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: List[int], k: int, queries: List[Tuple[int, int]]) -> List[int]:
        n = len(s)
        prefix_zero = [0] * (n + 1)
        prefix_one = [0] * (n + 1)

        for i in range(n):
            prefix_zero[i + 1] = prefix_zero[i] + (1 if s[i] == 0 else 0)
            prefix_one[i + 1] = prefix_one[i] + (1 if s[i] == 1 else 0)

        def count_valid_substrings(l: int, r: int) -> int:
            total = 0
            start = l
            while start <= r:
                low, high = start, r + 1
                while low < high:
                    mid = (low + high) // 2
                    zero_count = prefix_zero[mid + 1] - prefix_zero[start]
                    one_count = prefix_one[mid + 1] - prefix_one[start]
                    if zero_count > k and one_count > k:
                        high = mid
                    else:
                        low = mid + 1
                end_pos = low - 1
                if end_pos >= start:
                    total += end_pos - start + 1
                start += 1
            return total

        result = []
        for left, right in queries:
            result.append(count_valid_substrings(left, right))

        return result