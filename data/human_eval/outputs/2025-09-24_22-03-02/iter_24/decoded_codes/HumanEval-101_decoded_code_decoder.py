def words_string(s: str) -> list[str]:
    if s == "":
        return [""]

    s_list = []

    index = 0
    while index < len(s):
        letter = s[index]
        if letter == ",":
            s_list.append(" ")
        else:
            s_list.append(letter)
        index += 1

    joined_string = ""
    index = 0
    while index < len(s_list):
        joined_string += s_list[index]
        index += 1

    result = []
    current_word = ""
    index = 0
    while index < len(joined_string):
        current_character = joined_string[index]
        if current_character == " ":
            if current_word != "":
                result.append(current_word)
                current_word = ""
        else:
            current_word += current_character
        index += 1
    if current_word != "":
        result.append(current_word)

    return result