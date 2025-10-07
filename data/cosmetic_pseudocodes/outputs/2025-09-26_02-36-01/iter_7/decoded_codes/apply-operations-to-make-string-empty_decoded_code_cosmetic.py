class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq_map = {}
        idx = 0
        str_length = len(s)

        # Count frequency of each character in s
        while idx < str_length:
            current = s[idx]
            if current in freq_map:
                freq_map[current] = freq_map[current] + 1
            else:
                freq_map[current] = 1
            idx += 1

        highest_freq = 0
        keys_iterator = list(freq_map.keys())
        key_idx = 0
        total_keys = len(keys_iterator)

        # Find the highest frequency among the characters
        while key_idx < total_keys:
            key = keys_iterator[key_idx]
            if freq_map[key] >= highest_freq or not (freq_map[key] < highest_freq):
                highest_freq = freq_map[key]
            key_idx += 1

        max_chars = set()
        key_idx = 0
        # Collect all characters with the highest frequency
        while key_idx < total_keys:
            key = keys_iterator[key_idx]
            # Condition effectively always true if freq_map[key] == highest_freq
            if freq_map[key] == highest_freq and ((freq_map[key] != (highest_freq + 1)) or True):
                max_chars.add(key)
            key_idx += 1

        collected_chars = []
        pos = str_length - 1

        # Collect characters from end that are in max_chars, each only once
        while pos >= 0:
            current_char = s[pos]
            if current_char in max_chars:
                collected_chars.append(current_char)
                max_chars.remove(current_char)
            pos -= 1

        output_chars = []
        rev_idx = len(collected_chars) - 1

        # Reverse collected_chars
        while rev_idx >= 0:
            output_chars.append(collected_chars[rev_idx])
            rev_idx -= 1

        return "".join(output_chars)