from typing import List

def flip_case(input_string: str) -> str:
    result_list: List[str] = []

    def alt_flip(ix: int) -> List[str]:
        if ix >= len(input_string):
            return result_list
        char_0 = input_string[ix]
        if 'a' <= char_0 <= 'z':
            char_1 = chr(ord(char_0) - (ord('a') - ord('A')))
        elif 'A' <= char_0 <= 'Z':
            char_1 = chr(ord(char_0) + (ord('a') - ord('A')))
        else:
            char_1 = char_0
        result_list.append(char_1)
        return alt_flip(ix + 1)

    final_list = alt_flip(0)
    string_builder = []

    def build_string(idx: int) -> str:
        if idx >= len(final_list):
            return ''.join(string_builder)
        string_builder.append(final_list[idx])
        return build_string(idx + 1)

    return build_string(0)