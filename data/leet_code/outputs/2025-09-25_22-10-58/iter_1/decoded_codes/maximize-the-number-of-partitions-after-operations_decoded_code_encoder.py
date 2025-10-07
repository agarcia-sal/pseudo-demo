from string import ascii_lowercase

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            count = 0
            distinct_chars = set()
            for ch in s:
                if len(distinct_chars) < k:
                    distinct_chars.add(ch)
                elif ch in distinct_chars:
                    continue
                else:
                    count += 1
                    distinct_chars = {ch}
            if distinct_chars:
                count += 1
            return count

        max_parts = max_partitions(s, k)
        for i in range(len(s)):
            original_char = s[i]
            for new_char in ascii_lowercase:
                if new_char == original_char:
                    continue
                new_s = s[:i] + new_char + s[i+1:]
                max_parts = max(max_parts, max_partitions(new_s, k))

        return max_parts