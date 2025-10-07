class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def max_partitions(s: str, k: int) -> int:
            accumulator = 0
            unique_set = set()
            characters_list = list(s)

            def process_chars(index: int) -> int:
                if index >= len(characters_list):
                    return 0
                current_char = characters_list[index]
                if len(unique_set) < k:
                    unique_set.add(current_char)
                    return process_chars(index + 1)
                else:
                    if current_char in unique_set:
                        return process_chars(index + 1)
                    else:
                        nonlocal accumulator
                        accumulator += 1
                        unique_set.clear()
                        unique_set.add(current_char)
                        return process_chars(index + 1)

            result = process_chars(0)
            accumulator += result
            if len(unique_set) != 0:
                accumulator += 1
            return accumulator

        best_count = max_partitions(s, k)
        alphabet = [chr(c) for c in range(ord('a'), ord('z') + 1)]

        for outer_index in range(len(s)):
            current_pos_char = s[outer_index]
            for candidate_char in alphabet:
                if candidate_char == current_pos_char:
                    continue
                prefix = s[:outer_index]
                suffix = s[outer_index + 1:]
                new_candidate = prefix + candidate_char + suffix
                comparison_val = max_partitions(new_candidate, k)
                if comparison_val > best_count:
                    best_count = comparison_val
        return best_count