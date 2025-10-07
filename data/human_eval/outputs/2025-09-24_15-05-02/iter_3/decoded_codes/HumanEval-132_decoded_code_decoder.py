def is_nested(string: str) -> bool:
    opening_bracket_indices = []
    closing_bracket_indices = []

    # Collect indices of '[' and non-'[' characters
    for i, char in enumerate(string):
        if char == '[':
            opening_bracket_indices.append(i)
        else:
            closing_bracket_indices.append(i)

    # Reverse the list of closing bracket indices
    closing_bracket_indices.reverse()

    count = 0
    i = 0
    length_closing = len(closing_bracket_indices)

    # Count pairs where an opening bracket index is less than a closing bracket index
    for open_idx in opening_bracket_indices:
        if i < length_closing and open_idx < closing_bracket_indices[i]:
            count += 1
            i += 1

    return count >= 2