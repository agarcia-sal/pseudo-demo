from typing import List

def words_string(input_string: str) -> List[str]:
    result_words: List[str] = []
    if input_string != "":
        temp_chars: List[str] = []
        idx: int = 0
        while idx < len(input_string):
            current_char = input_string[idx]
            if current_char == ",":
                temp_chars.append(" ")
            else:
                temp_chars.append(current_char)
            idx += 1

        merged_text = "".join(temp_chars)
        result_words = merged_text.split()
    return result_words