from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        char_freq = defaultdict(int)
        last_letter = ""
        digit_accumulator = 0
        index = 0
        length = len(compressed)

        while index < length:
            current_element = compressed[index]
            if ('a' <= current_element <= 'z') or ('A' <= current_element <= 'Z'):
                if last_letter != "":
                    char_freq[last_letter] += digit_accumulator
                last_letter = current_element
                digit_accumulator = 0
            else:
                digit_accumulator = digit_accumulator * 10 + int(current_element)
            index += 1

        if last_letter != "":
            char_freq[last_letter] += digit_accumulator

        result_parts = []
        sorted_chars = sorted(char_freq.keys())

        for ch in sorted_chars:
            val = char_freq[ch]
            if val == 0:
                val_str = "0"
            else:
                val_str = ""
                while val > 0:
                    digit = val % 10
                    val_str = str(digit) + val_str
                    val //= 10
            result_parts.append(ch + val_str)

        better_compressed = "".join(result_parts)
        return better_compressed