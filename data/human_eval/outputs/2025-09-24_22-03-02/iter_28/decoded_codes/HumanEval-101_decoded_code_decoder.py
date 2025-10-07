def words_string(s) -> list:
    if s == "":
        return [""]
    s_list = []
    for index in range(len(s)):
        letter = s[index]
        if letter == ",":
            s_list.append(" ")
        else:
            s_list.append(letter)
    joined_string = ""
    for index in range(len(s_list)):
        joined_string += s_list[index]
    result_list = [""]
    current_word = ""
    for index in range(len(joined_string)):
        current_char = joined_string[index]
        if current_char == " ":
            if current_word != "":
                result_list.append(current_word)
                current_word = ""
        else:
            current_word += current_char
    if current_word != "":
        result_list.append(current_word)
    return result_list