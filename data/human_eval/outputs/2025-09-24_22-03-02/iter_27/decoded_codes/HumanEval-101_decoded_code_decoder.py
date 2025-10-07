from typing import List

def words_string(s: str) -> List[str]:
    if s == "":
        return [""]
    s_list = []
    for index in range(len(s)):
        letter = s[index]
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)
    joined_string = ""
    for index in range(len(s_list)):
        joined_string += s_list[index]
    words = []
    current_word = ""
    for index in range(len(joined_string)):
        current_character = joined_string[index]
        if current_character == ' ':
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += current_character
    if current_word != "":
        words.append(current_word)
    return words