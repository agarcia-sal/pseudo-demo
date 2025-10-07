def is_nested(string) -> bool:
    opening_bracket_index = []
    closing_bracket_index = []
    length_of_string = len(string)
    i = 0
    while i < length_of_string:
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
        i += 1
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    idx_index = 0
    while idx_index < len(opening_bracket_index):
        idx = opening_bracket_index[idx_index]
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
        idx_index += 1
    return cnt >= 2