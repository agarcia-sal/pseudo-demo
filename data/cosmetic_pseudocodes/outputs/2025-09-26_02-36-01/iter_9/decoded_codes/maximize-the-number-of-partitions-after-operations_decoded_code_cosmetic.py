class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:

        def max_partitions(s: str, k: int) -> int:
            accumulator = 0
            unique_set = set()

            index_tracker = 0
            while index_tracker < len(s):
                current_char = s[index_tracker]

                if len(unique_set) < k:
                    unique_set.add(current_char)
                else:
                    if current_char not in unique_set:
                        accumulator += 1
                        unique_set = {current_char}
                index_tracker += 1

            if len(unique_set) != 0:
                accumulator += 1

            return accumulator

        maximal_parts = max_partitions(s, k)

        outer_counter = 0
        alphabet_chars = "abcdefghijklmnopqrstuvwxyz"
        while outer_counter <= len(s) - 1:
            alphabet_iterator = 0

            while True:
                if alphabet_iterator >= len(alphabet_chars):
                    break

                candidate_char = alphabet_chars[alphabet_iterator]

                if candidate_char == s[outer_counter]:
                    alphabet_iterator += 1
                    continue

                prefix_str = s[:outer_counter]
                suffix_str = s[outer_counter + 1:]
                candidate_string = prefix_str + candidate_char + suffix_str

                current_max = max_partitions(candidate_string, k)
                if maximal_parts < current_max:
                    maximal_parts = current_max

                alphabet_iterator += 1

            outer_counter += 1

        return maximal_parts