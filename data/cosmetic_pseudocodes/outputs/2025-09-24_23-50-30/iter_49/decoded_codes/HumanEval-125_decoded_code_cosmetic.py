from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    def break_on_whitespace(sequence: str) -> List[str]:
        return sequence.split()

    def count_even_ascii_lowercase(sequence: List[str]) -> int:
        tally = 0
        for item in sequence:
            if item.islower() and (ord(item) % 2 == 0):
                tally += 1
        return tally

    def replace_commas_with_spaces(textual: str) -> str:
        return textual.replace(",", " ")

    if ' ' in input_string:
        return break_on_whitespace(input_string)
    elif ',' in input_string:
        return break_on_whitespace(replace_commas_with_spaces(input_string))
    else:
        return count_even_ascii_lowercase(list(input_string))