def is_nested(string: str) -> bool:
    opening_bracket_indices = []
    closing_bracket_indices = []

    for index, character in enumerate(string):
        if character == '[':
            opening_bracket_indices.append(index)
        else:
            closing_bracket_indices.append(index)

    closing_bracket_indices.reverse()

    matched_count = 0
    close_index = 0
    total_closing = len(closing_bracket_indices)

    for open_index in opening_bracket_indices:
        if close_index < total_closing and open_index < closing_bracket_indices[close_index]:
            matched_count += 1
            close_index += 1

    return matched_count >= 2