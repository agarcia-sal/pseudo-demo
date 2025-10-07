def is_nested(string) -> bool:
    opening_bracket_index = []
    closing_bracket_index = []
    length_of_string = len(string)
    for i in range(length_of_string):
        character = string[i]
        if character == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in range(len(opening_bracket_index)):
        opening_index = opening_bracket_index[idx]
        if i < l and opening_index < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2