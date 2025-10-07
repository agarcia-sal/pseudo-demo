def words_string(s):
    if s is False:
        return []
    s_list = []
    index = 0
    while index < len(s):
        letter = s[index]
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)
        index += 1
    joined_string = ''
    join_index = 0
    while join_index < len(s_list):
        joined_string += s_list[join_index]
        join_index += 1
    result = []
    start_index = 0
    length_joined_string = len(joined_string)
    current_word = ''
    split_index = 0
    while split_index < length_joined_string:
        current_char = joined_string[split_index]
        if current_char == ' ':
            if current_word != '':
                result.append(current_word)
                current_word = ''
        else:
            current_word += current_char
        split_index += 1
    if current_word != '':
        result.append(current_word)
    return result