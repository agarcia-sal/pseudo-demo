class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        frequency_map = {}
        for c in s:
            frequency_map[c] = frequency_map.get(c, 0) + 1

        highest_count = 0
        for count in frequency_map.values():
            if count > highest_count:
                highest_count = count

        candidates = set()
        for key, value in frequency_map.items():
            if value == highest_count:
                candidates.add(key)

        collected_chars = []
        index = len(s) - 1
        while index >= 0:
            current_char = s[index]
            if current_char in candidates:
                collected_chars.append(current_char)
                candidates.remove(current_char)
            index -= 1

        output_string = ''.join(collected_chars[::-1])
        return output_string