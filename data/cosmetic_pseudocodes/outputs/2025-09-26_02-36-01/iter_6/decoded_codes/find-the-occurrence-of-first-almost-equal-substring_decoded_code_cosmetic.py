class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            mismatch_counter = 0

            def recursive_compare(position0: int, limit0: int) -> bool:
                nonlocal mismatch_counter
                if position0 >= limit0:
                    return True
                char_a = substring[position0]
                char_b = pattern[position0]
                if char_a != char_b:
                    mismatch_counter += 1
                    if mismatch_counter > 1:
                        return False
                return recursive_compare(position0 + 1, limit0)

            return recursive_compare(0, len(pattern))

        pat_len = len(pattern)
        str_len = len(s)
        start_idx = 0
        found_index = -1
        while start_idx <= str_len - pat_len:
            if is_almost_equal(s[start_idx:start_idx + pat_len], pattern):
                found_index = start_idx
                break
            start_idx += 1
        return found_index