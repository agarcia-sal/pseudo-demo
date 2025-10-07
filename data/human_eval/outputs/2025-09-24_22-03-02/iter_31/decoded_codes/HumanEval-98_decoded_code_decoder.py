def count_upper(s):
    count = 0
    index_range = []
    length_s = len(s)
    current_index = 0
    while current_index < length_s:
        index_range.append(current_index)
        current_index += 2
    position = 0
    while position < len(index_range):
        i = index_range[position]
        character = s[i]
        if character in {"A", "E", "I", "O", "U"}:
            count += 1
        position += 1
    return count