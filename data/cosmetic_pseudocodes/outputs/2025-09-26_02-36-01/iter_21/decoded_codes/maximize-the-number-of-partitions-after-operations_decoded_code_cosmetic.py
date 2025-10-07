class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            count = 0
            unique_chars = set()
            for c in s:
                if len(unique_chars) < k:
                    unique_chars.add(c)
                else:
                    if c not in unique_chars:
                        count += 1
                        unique_chars = {c}
            if unique_chars:
                count += 1
            return count

        p9 = max_partitions(s, k)
        i8 = 0
        n = len(s)
        while i8 < n:
            for l1 in range(25, -1, -1):
                new_char = chr(97 + l1)
                if new_char == s[i8]:
                    continue
                new_s = s[:i8] + new_char + s[i8 + 1 :]
                w5 = max_partitions(new_s, k)
                if w5 > p9:
                    p9 = w5
            i8 += 1
        return p9