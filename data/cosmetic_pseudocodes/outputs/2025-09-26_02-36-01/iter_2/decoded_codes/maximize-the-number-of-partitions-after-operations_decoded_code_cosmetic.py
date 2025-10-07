class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            partition_count = 0
            unique_chars = set()
            idx = 0
            n = len(s)
            while idx < n:
                current_char = s[idx]
                if len(unique_chars) < k:
                    unique_chars.add(current_char)
                else:
                    if current_char in unique_chars:
                        idx += 1
                        continue
                    else:
                        partition_count += 1
                        unique_chars = {current_char}
                idx += 1
            if unique_chars:
                partition_count += 1
            return partition_count

        max_result = max_partitions(s, k)
        n = len(s)
        for i in range(n):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                if letter == s[i]:
                    continue
                new_string = s[:i] + letter + s[i+1:]
                max_result = max(max_result, max_partitions(new_string, k))
        return max_result