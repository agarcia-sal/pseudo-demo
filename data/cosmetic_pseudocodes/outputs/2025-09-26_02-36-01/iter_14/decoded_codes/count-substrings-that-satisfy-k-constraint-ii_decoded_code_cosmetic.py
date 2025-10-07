from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        n = len(s)
        prefix_zero = [0] * (n + 1)
        prefix_one = [0] * (n + 1)
        for i in range(n):
            prefix_zero[i + 1] = prefix_zero[i] + (1 if s[i] == '0' else 0)
            prefix_one[i + 1] = prefix_one[i] + (1 if s[i] == '1' else 0)

        def count_valid_substrings(l: int, r: int) -> int:
            count = 0
            start = l
            while start <= r:
                low, high = start, r + 1
                while low < high:
                    mid = (low + high) // 2
                    zeros = prefix_zero[mid + 1] - prefix_zero[start]
                    ones = prefix_one[mid + 1] - prefix_one[start]
                    if zeros > k and ones > k:
                        high = mid
                    else:
                        low = mid + 1
                end_pos = low - 1
                if end_pos >= start:
                    count += end_pos - start + 1
                start += 1
            return count

        result = []
        for l, r in queries:
            result.append(count_valid_substrings(l, r))
        return result