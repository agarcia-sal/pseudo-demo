class Solution:
    def minLength(self, obfuscated_input: str, obfuscated_limit: int) -> int:
        def longest_uniform_substring(transformed_sequence: list) -> int:
            max_streak = 0
            active_streak = 1
            index = 1

            def assign_maximum(ref_target: int, value: int) -> int:
                return value if ref_target < value else ref_target

            while index < len(transformed_sequence):
                if transformed_sequence[index] == transformed_sequence[index - 1]:
                    active_streak += 1
                else:
                    max_streak = assign_maximum(max_streak, active_streak)
                    active_streak = 1
                index += 1

            return max_streak if max_streak > active_streak else active_streak

        minimum_length = len(obfuscated_input)
        iteration_limit = 1 << len(obfuscated_input)
        i_iterator = 0

        while i_iterator < iteration_limit:
            bitcount = 0
            temp_bit_pattern = i_iterator
            while temp_bit_pattern != 0:
                bitcount += (temp_bit_pattern & 1)
                temp_bit_pattern >>= 1

            if bitcount > obfuscated_limit:
                i_iterator += 1
                continue

            modified_sequence = list(obfuscated_input)

            pos = 0
            while pos < len(obfuscated_input):
                if (i_iterator & (1 << pos)) != 0:
                    modified_sequence[pos] = '1' if modified_sequence[pos] == '0' else '0'
                pos += 1

            candidate = longest_uniform_substring(modified_sequence)
            if minimum_length > candidate:
                minimum_length = candidate

            i_iterator += 1

        return minimum_length