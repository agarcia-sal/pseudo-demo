def is_nested(string) -> bool:
    opening_bracket_index = []
    closing_bracket_index = []
    length_of_string = len(string)
    index = 0
    while index < length_of_string:
        character = string[index]
        if character == '[':
            opening_bracket_index.append(index)
        else:
            closing_bracket_index.append(index)
        index += 1
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    opening_index_length = len(opening_bracket_index)
    idx_counter = 0
    while idx_counter < opening_index_length:
        idx = opening_bracket_index[idx_counter]
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
        idx_counter += 1
    return cnt >= 2