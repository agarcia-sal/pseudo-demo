from typing import List


def anti_shuffle(cipher: str) -> str:
    tokens: List[str] = cipher.split(" ")
    rearranged: List[str] = []
    position: int = 0
    while position < len(tokens):
        current_token: str = tokens[position]
        chars_list: List[str] = list(current_token)

        indexer: int = 1
        while indexer < len(chars_list):
            key_char: str = chars_list[indexer]
            cursor: int = indexer - 1
            while cursor >= 0 and chars_list[cursor] > key_char:
                # Swap chars_list[cursor + 1] and chars_list[cursor]
                temp_char: str = chars_list[cursor + 1]
                chars_list[cursor + 1] = chars_list[cursor]
                chars_list[cursor] = temp_char
                cursor -= 1
            indexer += 1

        sorted_token: str = ""
        char_pos: int = 0
        while char_pos < len(chars_list):
            sorted_token += chars_list[char_pos]
            char_pos += 1

        rearranged.append(sorted_token)
        position += 1

    outcome: str = ""
    idx: int = 0
    while idx < len(rearranged):
        outcome += rearranged[idx]
        if idx != len(rearranged) - 1:
            outcome += " "
        idx += 1

    return outcome