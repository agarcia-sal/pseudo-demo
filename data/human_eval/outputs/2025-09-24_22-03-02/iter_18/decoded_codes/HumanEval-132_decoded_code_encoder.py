def is_nested(string) -> bool:
    opening_bracket_index = []
    closing_bracket_index = []
    string_length = len(string)
    index_i = 0
    while index_i < string_length:
        current_char = string[index_i]
        if current_char == '[':
            opening_bracket_index.append(index_i)
        else:
            closing_bracket_index.append(index_i)
        index_i += 1
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    idx_position_index = 0
    while idx_position_index < len(opening_bracket_index):
        idx = opening_bracket_index[idx_position_index]
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
        idx_position_index += 1
    return cnt >= 2