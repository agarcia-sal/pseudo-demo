from collections import Counter

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        char_count = Counter(s)
        max_freq = max(char_count.values(), default=0)
        max_freq_chars = {char for char, count in char_count.items() if count == max_freq}
        result = []
        for char in reversed(s):
            if char in max_freq_chars:
                result.append(char)
                max_freq_chars.remove(char)
        return ''.join(reversed(result))