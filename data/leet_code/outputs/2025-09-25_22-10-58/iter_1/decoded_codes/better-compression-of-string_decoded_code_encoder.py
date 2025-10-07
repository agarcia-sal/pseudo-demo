from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        char_count = defaultdict(int)
        current_char = ''
        current_count = 0
        for ch in compressed:
            if ch.isalpha():
                if current_char != '':
                    char_count[current_char] += current_count
                current_char = ch
                current_count = 0
            else:
                current_count = current_count * 10 + int(ch)
        if current_char != '':
            char_count[current_char] += current_count
        better_compressed_parts = []
        for ch in sorted(char_count.keys()):
            better_compressed_parts.append(ch + str(char_count[ch]))
        return ''.join(better_compressed_parts)