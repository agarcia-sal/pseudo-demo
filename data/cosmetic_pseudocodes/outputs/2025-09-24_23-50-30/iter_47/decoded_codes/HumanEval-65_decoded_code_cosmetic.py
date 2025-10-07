def circular_shift(integer_x: int, integer_shift: int) -> str:
    string_buffer = str(integer_x)
    total_length = len(string_buffer)

    if integer_shift > total_length:
        # Reverse the string_buffer
        idx1 = total_length - 1
        buffer_chars = []
        while idx1 >= 0:
            buffer_chars.append(string_buffer[idx1])
            idx1 -= 1
        return "".join(buffer_chars)

    pivot = total_length - integer_shift
    buffer_chars = []
    counter = 0
    while counter < integer_shift:
        buffer_chars.append(string_buffer[pivot + counter])
        counter += 1
    index = 0
    while index < pivot:
        buffer_chars.append(string_buffer[index])
        index += 1
    return "".join(buffer_chars)