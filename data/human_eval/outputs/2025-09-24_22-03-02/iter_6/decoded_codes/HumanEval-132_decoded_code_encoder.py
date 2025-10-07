def is_nested(string) -> bool:
    opening_bracket_index = []
    closing_bracket_index = []

    for position in range(len(string)):
        if string[position] == '[':
            opening_bracket_index.append(position)
        else:
            closing_bracket_index.append(position)

    closing_bracket_index.reverse()

    count = 0
    index = 0
    total_closing = len(closing_bracket_index)

    for opening_position in opening_bracket_index:
        if index < total_closing and opening_position < closing_bracket_index[index]:
            count += 1
            index += 1

    return count >= 2