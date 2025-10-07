from typing import List


def words_string(text_input: str) -> List[str]:
    char_collection: List[str] = []

    idx: int = 0
    while idx < len(text_input):
        current_char: str = text_input[idx]

        if current_char == ',':
            char_collection.append(' ')
        else:
            char_collection.append(current_char)

        idx += 1

    combined: str = ""
    pos: int = 0
    while pos < len(char_collection):
        combined += char_collection[pos]
        pos += 1

    if combined == "":
        return []
    else:
        word_list: List[str] = []
        start_pos: int = 0
        curr_pos: int = 0
        while curr_pos <= len(combined):
            if curr_pos == len(combined) or combined[curr_pos] == ' ':
                if start_pos < curr_pos:
                    word_list.append(combined[start_pos:curr_pos])
                start_pos = curr_pos + 1
            curr_pos += 1
        return word_list