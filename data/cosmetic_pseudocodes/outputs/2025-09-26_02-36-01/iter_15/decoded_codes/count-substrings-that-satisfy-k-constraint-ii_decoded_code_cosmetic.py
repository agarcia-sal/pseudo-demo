from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        n = len(s)
        zeros_prefix = [0] * (n + 1)
        ones_prefix = [0] * (n + 1)
        for i in range(n):
            zeros_prefix[i + 1] = zeros_prefix[i] + (1 if s[i] == '0' else 0)
            ones_prefix[i + 1] = ones_prefix[i] + (1 if s[i] == '1' else 0)

        def count_valid_substrings(l: int, r: int) -> int:
            total_valid = 0
            current_start = l
            while current_start <= r:
                low, high = current_start, r + 1
                while low < high:
                    mid = (low + high) // 2
                    zero_count = zeros_prefix[mid + 1] - zeros_prefix[current_start]
                    one_count = ones_prefix[mid + 1] - ones_prefix[current_start]
                    if zero_count <= k or one_count <= k:
                        low = mid + 1
                    else:
                        high = mid
                valid_endpoint = low - 1
                if valid_endpoint >= current_start:
                    total_valid += valid_endpoint - current_start + 1
                current_start += 1
            return total_valid

        result = []
        for l, r in queries:
            result.append(count_valid_substrings(l, r))
        return result