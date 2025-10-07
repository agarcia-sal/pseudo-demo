from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isAlpha(ch: str) -> bool:
            return ("A" <= ch <= "Z") or ("a" <= ch <= "z")

        frequency_map = defaultdict(int)
        char_holder = ""
        number_accumulator = 0

        def processChar():
            nonlocal char_holder, number_accumulator, frequency_map
            if char_holder != "":
                frequency_map[char_holder] += number_accumulator

        index_var = 0
        length = len(compressed)
        while index_var < length:
            current_element = compressed[index_var]
            if isAlpha(current_element):
                processChar()
                char_holder = current_element
                number_accumulator = 0
            else:
                number_accumulator = number_accumulator * 10 + (ord(current_element) - ord("0"))
            index_var += 1

        processChar()

        sorted_chars = sorted(frequency_map.keys())

        parts_list = []
        for temp_key in sorted_chars:
            temp_val = frequency_map[temp_key]

            def intToStr(num: int) -> str:
                if num == 0:
                    return "0"
                res_str = ""
                while num > 0:
                    digit_char = chr((num % 10) + ord("0"))
                    res_str = digit_char + res_str
                    num //= 10
                return res_str

            concatenated_piece = temp_key + intToStr(temp_val)
            parts_list.append(concatenated_piece)

        result_str = "".join(parts_list)
        return result_str