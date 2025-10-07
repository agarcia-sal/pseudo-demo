from typing import List

def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    result_array: List[str] = []
    for idx in range(len(input_string)):
        current_char = input_string[idx]
        if current_char != ",":
            result_array.append(current_char)
        else:
            result_array.append(" ")

    merged_text = "".join(result_array)

    output_words: List[str] = []
    temp_word = ""
    for ch in merged_text:
        if ch in {" ", "\t", "\n"}:
            if temp_word != "":
                output_words.append(temp_word)
                temp_word = ""
        else:
            temp_word += ch
    if temp_word != "":
        output_words.append(temp_word)

    return output_words