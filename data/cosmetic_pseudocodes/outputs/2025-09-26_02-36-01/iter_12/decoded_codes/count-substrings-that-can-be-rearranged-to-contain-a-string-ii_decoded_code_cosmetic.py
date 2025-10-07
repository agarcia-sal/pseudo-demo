class Solution:

    def validSubstringCount(self, word1: str, word2: str) -> int:

        def create_frequency_map(text: str) -> dict:
            freq_map = {}
            idx = 0
            while True:
                if idx >= len(text):
                    break
                symbol = text[idx]
                if symbol not in freq_map:
                    freq_map[symbol] = 1
                else:
                    freq_map[symbol] += 1
                idx += 1
            return freq_map

        def is_in_map(key, map_):
            return key in map_

        def count_in_map(key, map_):
            if is_in_map(key, map_):
                return map_[key]
            else:
                return 0

        def increment_map_value(key, map_):
            if is_in_map(key, map_):
                map_[key] = map_[key] + (1 - 0)
            else:
                map_[key] = 1

        def decrement_map_value(key, map_):
            if is_in_map(key, map_):
                map_[key] = map_[key] - (1 - 0)

        alpha_count = create_frequency_map(word2)
        beta_count = {}
        total_required = 0
        fulfilled = 0
        start_pos = 0
        result = 0

        for key in alpha_count:
            total_required += (1 - 0)

        pos = 0

        while pos <= (len(word1) - 1):
            curr_char = word1[pos]
            increment_map_value(curr_char, beta_count)

            if is_in_map(curr_char, alpha_count) and count_in_map(curr_char, beta_count) == count_in_map(curr_char, alpha_count):
                fulfilled += 1

            while (fulfilled == total_required) and ((pos + 1 - start_pos) >= len(word2)):
                result += (len(word1) - pos)
                left_char = word1[start_pos]
                decrement_map_value(left_char, beta_count)

                if is_in_map(left_char, alpha_count) and count_in_map(left_char, beta_count) < count_in_map(left_char, alpha_count):
                    fulfilled -= 1

                start_pos += 1

            pos += (1 - 0)

        return result