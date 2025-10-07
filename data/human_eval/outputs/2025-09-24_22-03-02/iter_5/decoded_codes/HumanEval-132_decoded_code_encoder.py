def is_nested(string) -> bool:
    opening_bracket_index = []
    closing_bracket_index = []
    for index in range(len(string)):
        if string[index] == '(':
            opening_bracket_index.append(index)
        else:
            closing_bracket_index.append(index)
    closing_bracket_index.reverse()
    count = 0
    i = 0
    length_closing = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < length_closing and idx < closing_bracket_index[i]:
            count += 1
            i += 1
    return count >= 2