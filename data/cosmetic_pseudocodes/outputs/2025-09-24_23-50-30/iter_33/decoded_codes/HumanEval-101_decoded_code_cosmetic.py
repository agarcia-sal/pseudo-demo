from typing import List


def words_string(input_string: str) -> List[str]:
    def transform_indexed(idx: int, limit: int, acc: str) -> str:
        if not (idx < limit):
            return acc
        current_char = input_string[idx]
        return transform_indexed(idx + 1, limit, acc + (' ' if current_char == ',' else current_char))

    if input_string == '':
        return []
    result_string = transform_indexed(0, len(input_string), '')
    output_words: List[str] = []
    pos = 0
    len_str = len(result_string)

    while pos < len_str:
        while pos < len_str and result_string[pos] == ' ':
            pos += 1
        if pos >= len_str:
            break
        start = pos
        while pos < len_str and result_string[pos] != ' ':
            pos += 1
        output_words.append(result_string[start:pos])
    return output_words