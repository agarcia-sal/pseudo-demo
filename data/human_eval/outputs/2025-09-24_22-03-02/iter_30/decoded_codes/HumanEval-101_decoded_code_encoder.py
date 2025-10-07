def words_string(s) -> list:
    if s == "":
        return [""]

    s_list = []
    index = 0
    while index < len(s):
        letter = s[index]
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)
        index += 1

    concatenated_string = ""
    index = 0
    while index < len(s_list):
        concatenated_string += s_list[index]
        index += 1

    result_list = concatenated_string.split()
    return result_list