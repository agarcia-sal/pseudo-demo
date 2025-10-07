def is_nested(input_string):
    opening_bracket_indices = []
    closing_bracket_indices = []

    for index in range(len(input_string)):
        if input_string[index] == '[':
            opening_bracket_indices.append(index)
        else:
            closing_bracket_indices.append(index)

    closing_bracket_indices.reverse()

    count = 0
    i = 0
    length_closing = len(closing_bracket_indices)

    for idx in opening_bracket_indices:
        if i < length_closing and idx < closing_bracket_indices[i]:
            count += 1
            i += 1

    return count >= 2