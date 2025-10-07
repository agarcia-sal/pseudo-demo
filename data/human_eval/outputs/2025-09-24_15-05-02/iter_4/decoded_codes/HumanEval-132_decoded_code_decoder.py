def is_nested(string):
    opening_bracket_index = []
    closing_bracket_index = []

    for index, char in enumerate(string):
        if char == '[':
            opening_bracket_index.append(index)
        else:
            closing_bracket_index.append(index)

    closing_bracket_index.reverse()

    count = 0
    i = 0
    length_closing = len(closing_bracket_index)

    for open_index in opening_bracket_index:
        if i < length_closing and open_index < closing_bracket_index[i]:
            count += 1
            i += 1

    return count >= 2