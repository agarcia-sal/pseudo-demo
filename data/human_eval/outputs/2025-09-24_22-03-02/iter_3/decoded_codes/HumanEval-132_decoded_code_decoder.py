def is_nested(string):
    opening_bracket_index = [i for i, ch in enumerate(string) if ch == '[']
    closing_bracket_index = [i for i, ch in enumerate(string) if ch != '['][::-1]

    count = 0
    i = 0
    length_to_compare = len(closing_bracket_index)

    for idx in opening_bracket_index:
        if i < length_to_compare and idx < closing_bracket_index[i]:
            count += 1
            i += 1

    return count >= 2