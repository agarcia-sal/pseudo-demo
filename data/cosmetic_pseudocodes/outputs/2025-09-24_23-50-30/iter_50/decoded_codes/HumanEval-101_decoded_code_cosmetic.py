from typing import List


def words_string(original_text: str) -> List[str]:
    def transform(index: int, acc: List[str]) -> List[str]:
        if index >= len(original_text):
            return acc
        current_char = original_text[index]
        if current_char != ',':
            return transform(index + 1, acc + [current_char])
        else:
            return transform(index + 1, acc + [' '])

    replaced_chars: List[str] = transform(0, [])

    concatenated_text = "".join(replaced_chars)

    result_words: List[str] = []
    temp_buffer = []

    def add_word() -> None:
        if temp_buffer:
            result_words.append("".join(temp_buffer))

    for symbol in concatenated_text:
        if symbol in {' ', '\t', '\n'}:
            add_word()
            temp_buffer = []
        else:
            temp_buffer.append(symbol)
    add_word()

    return result_words