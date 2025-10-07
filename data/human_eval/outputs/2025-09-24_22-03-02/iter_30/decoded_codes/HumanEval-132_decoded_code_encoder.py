def is_nested(string: str) -> bool:
    opening_bracket_index = []
    closing_bracket_index = []
    length_of_string = len(string)
    index = 0
    while index < length_of_string:
        current_char = string[index]
        if current_char == '[':
            opening_bracket_index.append(index)
        else:
            closing_bracket_index.append(index)
        index += 1
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    pos = 0
    while pos < len(opening_bracket_index):
        idx = opening_bracket_index[pos]
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
        pos += 1
    return cnt >= 2