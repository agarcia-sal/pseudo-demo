from typing import List

def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    tokens: List[str] = []

    position = 0
    while position < len(input_string):
        current_char = input_string[position]
        if current_char == ',':
            tokens.append(' ')
        else:
            tokens.append(current_char)
        position += 1

    combined = "".join(tokens)
    return combined.split(" ")