from typing import List

def words_string(param_str: str) -> List[str]:
    if param_str:
        temp_chars: List[str] = []
        idx_counter: int = 0
        while idx_counter < len(param_str):
            current_char: str = param_str[idx_counter]
            if current_char == ',':
                temp_chars.append(' ')
            else:
                temp_chars.append(current_char)
            idx_counter += 1

        intermediate_string: str = ""
        temp_idx: int = 0
        while temp_idx < len(temp_chars):
            intermediate_string += temp_chars[temp_idx]
            temp_idx += 1

        result_words: List[str] = intermediate_string.split(' ')
    else:
        result_words = []

    return result_words