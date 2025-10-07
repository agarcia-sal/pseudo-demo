def is_nested(string: str) -> bool:
    opening_bracket_index = []
    closing_bracket_index = []
    string_length = len(string)
    for i in range(string_length):
        current_char = string[i]
        if current_char == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in range(len(opening_bracket_index)):
        current_open_idx = opening_bracket_index[idx]
        if i < l:
            current_close_idx = closing_bracket_index[i]
            if current_open_idx < current_close_idx:
                cnt += 1
                i += 1
    if cnt >= 2:
        return True
    else:
        return False