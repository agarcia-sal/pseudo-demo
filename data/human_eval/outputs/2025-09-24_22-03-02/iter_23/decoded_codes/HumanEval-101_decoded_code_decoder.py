from typing import List

def words_string(s: str) -> List[str]:
    if s == "":
        return [""]

    s_list = []

    for index in range(len(s)):
        letter = s[index]
        if letter == ",":
            s_list.append(" ")
        else:
            s_list.append(letter)

    s_list_str = ""
    for index in range(len(s_list)):
        s_list_str += s_list[index]

    result_list = []
    current_word = ""

    for index in range(len(s_list_str)):
        character = s_list_str[index]
        if character == " ":
            if current_word != "":
                result_list.append(current_word)
                current_word = ""
        else:
            current_word += character

    if current_word != "":
        result_list.append(current_word)

    return result_list