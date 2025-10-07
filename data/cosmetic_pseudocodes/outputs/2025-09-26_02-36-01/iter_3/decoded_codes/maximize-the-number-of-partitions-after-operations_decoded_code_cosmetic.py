class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            segment_count = 0
            char_set = set()
            index = 0
            while index < len(s):
                if len(char_set) < k:
                    char_set.add(s[index])
                else:
                    if s[index] not in char_set:
                        segment_count += 1
                        char_set = {s[index]}
                index += 1
            if len(char_set) > 0:
                segment_count += 1
            return segment_count

        best_partition = max_partitions(s, k)
        for position in range(len(s)):
            for letter_code in range(97, 123):
                alternative_char = chr(letter_code)
                if alternative_char != s[position]:
                    modified_string = s[:position] + alternative_char + s[position+1:]
                    candidate = max_partitions(modified_string, k)
                    if candidate > best_partition:
                        best_partition = candidate
        return best_partition