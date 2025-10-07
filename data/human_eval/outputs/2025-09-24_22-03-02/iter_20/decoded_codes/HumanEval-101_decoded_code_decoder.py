from typing import List, Optional

def words_string(s: Optional[str]) -> List[str]:
    if s == '' or s is None:
        return ['']

    s_list: List[str] = []

    for index in range(len(s)):
        letter = s[index]
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    joined_string = ''
    for index in range(len(s_list)):
        joined_string += s_list[index]

    result_list: List[str] = []
    current_word = ''

    for index in range(len(joined_string)):
        current_character = joined_string[index]
        if current_character == ' ':
            if current_word != '':
                result_list.append(current_word)
                current_word = ''
        else:
            current_word += current_character

    if current_word != '':
        result_list.append(current_word)

    return result_list