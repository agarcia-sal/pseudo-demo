class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            alpha_count = 0
            distinct_set = set()
            x = 0
            while x < len(s):
                ch = s[x]
                if len(distinct_set) < k:
                    distinct_set.add(ch)
                else:
                    if ch not in distinct_set:
                        alpha_count += 1
                        distinct_set = {ch}
                x += 1
            if distinct_set:
                alpha_count += 1
            return alpha_count

        max_parts = max_partitions(s, k)
        letters = "abcdefghijklmnopqrstuvwxyz"
        for pos_i in range(len(s)):
            for candidate_char in letters:
                if candidate_char == s[pos_i]:
                    continue
                prefix = s[:pos_i] if pos_i > 0 else ""
                suffix = s[pos_i+1:] if pos_i + 1 < len(s) else ""
                new_s = prefix + candidate_char + suffix
                candidate_count = max_partitions(new_s, k)
                if candidate_count > max_parts:
                    max_parts = candidate_count
        return max_parts