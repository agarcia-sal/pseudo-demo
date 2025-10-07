class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            partition_count = 0
            char_bucket = set()
            for ch in s:
                if len(char_bucket) < k:
                    char_bucket.add(ch)
                elif ch in char_bucket:
                    continue
                else:
                    partition_count += 1
                    char_bucket = {ch}
            if char_bucket:
                partition_count += 1
            return partition_count

        result = max_partitions(s, k)

        for index in range(len(s)):
            original_char = s[index]
            for replacement_char in map(chr, range(ord('a'), ord('z') + 1)):
                if replacement_char == original_char:
                    continue
                modified_s = s[:index] + replacement_char + s[index + 1:]
                result = max(result, max_partitions(modified_s, k))

        return result