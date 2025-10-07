from typing import List


def anti_shuffle(reference_str: str) -> str:
    tokens: List[str] = []
    position: int = 0  # zero-based index for Python

    length = len(reference_str)
    while position < length:
        # Skip leading spaces if any
        while position < length and reference_str[position] == ' ':
            position += 1
        if position >= length:
            break
        start_pos = position
        while position < length and reference_str[position] != ' ':
            position += 1
        tokens.append(reference_str[start_pos:position])
        position += 1  # skip space after word

    def reorder_word(chars_list: List[str]) -> List[str]:
        if len(chars_list) <= 1:
            return chars_list
        pivot = chars_list[1]
        less_sorted = reorder_word([x for x in chars_list if x < pivot])
        equal_chars = [x for x in chars_list if x == pivot]
        greater_sorted = reorder_word([x for x in chars_list if x > pivot])
        return less_sorted + equal_chars + greater_sorted

    result_words: List[str] = []
    for token in tokens:
        letters = [char for char in token]
        rearranged_letters = reorder_word(letters)
        rebuilt_word = ''.join(rearranged_letters)
        result_words.append(rebuilt_word)

    output = ' '.join(result_words)
    return output