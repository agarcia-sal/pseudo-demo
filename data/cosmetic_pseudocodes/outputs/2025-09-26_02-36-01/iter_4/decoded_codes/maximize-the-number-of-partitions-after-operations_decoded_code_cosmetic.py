class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            partition_count = 0
            collected_chars = set()
            index_counter = 0
            while index_counter < len(s):
                current_char = s[index_counter]
                if len(collected_chars) < k:
                    collected_chars.add(current_char)
                else:
                    if current_char not in collected_chars:
                        partition_count += 1
                        collected_chars = {current_char}
                index_counter += 1
            if collected_chars:
                partition_count += 1
            return partition_count

        max_parts = max_partitions(s, k)
        letters = [chr(c) for c in range(ord('a'), ord('z') + 1)]
        for pos in range(len(s)):
            for substitute_char in letters:
                if substitute_char == s[pos]:
                    continue
                new_s = s[:pos] + substitute_char + s[pos+1:]
                candidate_partition_count = max_partitions(new_s, k)
                if candidate_partition_count > max_parts:
                    max_parts = candidate_partition_count
        return max_parts