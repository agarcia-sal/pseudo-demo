from typing import List


def anti_shuffle(input_string: str) -> str:
    tokens: List[str] = input_string.split(" ")
    sorted_tokens: List[str] = []
    index: int = 0

    while index < len(tokens):
        char_list: List[str] = sorted(list(tokens[index]))
        assembled_word: str = "".join(char_list)
        sorted_tokens.append(assembled_word)
        index += 1

    output: str = ""
    if len(sorted_tokens) > 0:
        output = sorted_tokens[0]

    for position in range(1, len(sorted_tokens)):
        output += " " + sorted_tokens[position]

    return output