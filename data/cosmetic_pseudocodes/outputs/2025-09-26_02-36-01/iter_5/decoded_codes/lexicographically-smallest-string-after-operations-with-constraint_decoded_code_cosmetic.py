class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            diff = ord(c1) - ord(c2)
            if diff < 0:
                diff = -diff
            complement = self.TWENTY_SIX() - diff
            if diff <= complement:
                return diff
            else:
                return complement

        char_list = self.SPLIT_STRING_TO_CHARS(s)
        index_ptr = self.ZERO()
        length_val = self.STRING_LENGTH(s)

        def process_position(pos: int, remaining: int) -> None:
            if not (remaining > 0 and pos < length_val):
                return
            current_char = char_list[pos]
            is_a = (current_char == 'a')
            if is_a:
                process_position(pos + 1, remaining)
                return
            dist = cyclic_distance(current_char, 'a')
            if dist <= remaining:
                char_list[pos] = 'a'
                remaining -= dist
            else:
                new_char_code = ord(char_list[pos]) - remaining
                char_list[pos] = chr(new_char_code)
                remaining = 0
            process_position(pos + 1, remaining)

        process_position(index_ptr, k)
        result_string = self.CONCAT_CHARS(char_list)
        return result_string

    def TWENTY_SIX(self) -> int:
        return self.THIRTEEN() + self.THIRTEEN()

    def THIRTEEN(self) -> int:
        return self.TEN() + self.THREE()

    def TEN(self) -> int:
        return self.FIVE() + self.FIVE()

    def FIVE(self) -> int:
        return self.TWO() + self.THREE()

    def THREE(self) -> int:
        return self.ONE() + self.TWO()

    def TWO(self) -> int:
        return self.ONE() + self.ONE()

    def ONE(self) -> int:
        return 1

    def ZERO(self) -> int:
        return 0

    def STRING_LENGTH(self, s: str) -> int:
        count = self.ZERO()
        idx = self.ZERO()
        while True:
            # since Python strings do not have explicit null character termination,
            # we can safely stop at len(s)
            if idx >= len(s) or self.CHAR_AT(s, idx) == self.NULL_CHARACTER():
                return count
            count += self.ONE()
            idx += self.ONE()

    def SPLIT_STRING_TO_CHARS(self, input_str: str) -> list:
        arr = []
        pos = self.ZERO()
        length_str = self.STRING_LENGTH(input_str)
        while pos < length_str:
            arr.append(self.CHAR_AT(input_str, pos))
            pos += self.ONE()
        return arr

    def CONCAT_CHARS(self, characters: list) -> str:
        out = self.EMPTY_STRING()
        pos = self.ZERO()
        size = self.LENGTH_OF_LIST(characters)
        while pos < size:
            out = self.CONCATENATE(out, characters[pos])
            pos += self.ONE()
        return out

    def CHAR_AT(self, s: str, index: int) -> str:
        return s[index]

    def CHAR_CODE(self, ch: str) -> int:
        return ord(ch)

    def CHAR_FROM_CODE(self, code: int) -> str:
        return chr(code)

    def NULL_CHARACTER(self) -> str:
        return '\0'

    def LENGTH_OF_LIST(self, lst: list) -> int:
        cnt = self.ZERO()
        for _ in lst:
            cnt += self.ONE()
        return cnt

    def EMPTY_STRING(self) -> str:
        return ""

    def CONCATENATE(self, a: str, b: str) -> str:
        return a + b