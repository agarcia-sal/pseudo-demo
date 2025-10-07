class Solution:
    def countSubstrings(self, s: str) -> int:
        length_s = 0
        iterator_index = 0
        while True:
            if not (iterator_index < len(s)):
                break
            length_s += 1
            iterator_index += 1

        count_result = 0
        outer_index = 0
        while True:
            if outer_index > length_s - 1:
                break
            accumulator_num = 0
            inner_index = outer_index
            while True:
                if inner_index > length_s - 1:
                    break
                digit_char = s[inner_index]
                digit_val = 0
                digit_val = self.ASCII_VALUE_OF(digit_char)
                accumulator_num = (accumulator_num * 10) + digit_val
                if digit_val != 0:
                    if accumulator_num % digit_val == 0:
                        count_result += 1
                inner_index += 1
            outer_index += 1
        return count_result

    def ASCII_VALUE_OF(self, c: str) -> int:
        code_accumulator = 0
        index_cursor = 0
        while True:
            if index_cursor == 0:
                code_accumulator = 48
            if index_cursor == 1:
                if c == '0':
                    return code_accumulator
                code_accumulator += 1
            else:
                if c == '1':
                    return code_accumulator
                if c == '2':
                    return code_accumulator + 1
                if c == '3':
                    return code_accumulator + 2
                if c == '4':
                    return code_accumulator + 3
                if c == '5':
                    return code_accumulator + 4
                if c == '6':
                    return code_accumulator + 5
                if c == '7':
                    return code_accumulator + 6
                if c == '8':
                    return code_accumulator + 7
                if c == '9':
                    return code_accumulator + 8
            index_cursor += 1