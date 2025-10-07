class Solution:
    def betterCompression(self, compressed: str) -> str:
        from collections import defaultdict

        char_count = defaultdict(int)
        current_char = None
        current_count = 0

        for ch in compressed:
            if ch.isalpha():
                if current_char is not None:
                    char_count[current_char] += current_count
                current_char = ch
                current_count = 0
            else:
                current_count = current_count * 10 + int(ch)

        if current_char is not None:
            char_count[current_char] += current_count

        output_parts = []
        for character in sorted(char_count):
            output_parts.append(character + str(char_count[character]))

        return "".join(output_parts)