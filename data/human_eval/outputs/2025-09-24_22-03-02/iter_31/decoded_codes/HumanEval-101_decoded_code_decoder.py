from typing import List

def words_string(s: str) -> List[str]:
    if s == "":
        return [""]

    s_list = []
    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    joined_string = "".join(s_list)

    word_list = []
    current_word = ""
    for current_char in joined_string:
        if current_char == ' ':
            if current_word != "":
                word_list.append(current_word)
                current_word = ""
        else:
            current_word += current_char

    if current_word != "":
        word_list.append(current_word)

    return word_list