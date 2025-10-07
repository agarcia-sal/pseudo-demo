from typing import List

def anti_shuffle(obtained_text: str) -> str:
    extracted_tokens: List[str] = []
    temp_string: str = ""
    position: int = 0
    length_to_process: int = len(obtained_text)
    while position < length_to_process:
        current_char: str = obtained_text[position]
        if current_char == " ":
            extracted_tokens.append(temp_string)
            temp_string = ""
        else:
            temp_string += current_char
        position += 1
    if temp_string != "":
        extracted_tokens.append(temp_string)

    reordered_tokens: List[str] = []
    index_in_tokens: int = 0
    while index_in_tokens < len(extracted_tokens):
        token_to_sort: str = extracted_tokens[index_in_tokens]
        characters_list: List[str] = []
        char_index: int = 0
        length_token: int = len(token_to_sort)
        while char_index < length_token:
            characters_list.append(token_to_sort[char_index])
            char_index += 1

        swap_occurred: bool = True
        while swap_occurred:
            swap_occurred = False
            j: int = 0
            while j < len(characters_list) - 1:
                if ord(characters_list[j]) > ord(characters_list[j + 1]):
                    temp_char: str = characters_list[j]
                    characters_list[j] = characters_list[j + 1]
                    characters_list[j + 1] = temp_char
                    swap_occurred = True
                j += 1

        assembled_word: str = ""
        k: int = 0
        while k < len(characters_list):
            assembled_word += characters_list[k]
            k += 1

        reordered_tokens.append(assembled_word)
        index_in_tokens += 1

    final_result: str = ""
    m: int = 0
    length_reordered: int = len(reordered_tokens)
    while True:
        if m == length_reordered:
            break
        final_result += reordered_tokens[m]
        if m < length_reordered - 1:
            final_result += " "
        m += 1

    return final_result