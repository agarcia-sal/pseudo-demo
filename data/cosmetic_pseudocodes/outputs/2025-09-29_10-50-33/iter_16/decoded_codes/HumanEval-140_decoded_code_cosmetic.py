def fix_spaces(text: str) -> str:
    new_result = []
    position = 0
    segment_start = 0
    segment_end = 0
    length = len(text)

    while True:
        if position == length:
            break
        current_char = text[position]
        if current_char == ' ':
            segment_end += 1
        else:
            space_count = segment_end - segment_start
            if space_count > 2:
                new_result.append('-')
                new_result.append(current_char)
            elif space_count > 0:
                new_result.append('_' * space_count)
                new_result.append(current_char)
            else:
                new_result.append(current_char)
            segment_start = position + 1
            segment_end = position + 1
        position += 1

    trailing_spaces = segment_end - segment_start
    if trailing_spaces > 2:
        new_result.append('-')
    elif trailing_spaces > 0:
        new_result.append('_')

    return ''.join(new_result)