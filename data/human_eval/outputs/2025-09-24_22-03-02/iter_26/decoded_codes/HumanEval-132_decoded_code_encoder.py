def is_nested(string: str) -> bool:
    opening_bracket_index = []
    closing_bracket_index = []
    string_length = len(string)
    for i in range(string_length):
        current_character = string[i]
        if current_character == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx_index in range(len(opening_bracket_index)):
        idx = opening_bracket_index[idx_index]
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2