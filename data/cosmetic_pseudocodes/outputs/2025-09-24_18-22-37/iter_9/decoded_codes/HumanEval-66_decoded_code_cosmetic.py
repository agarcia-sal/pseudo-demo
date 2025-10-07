def digitSum(input_string: str) -> int:
    accumulator = 0
    position = 0
    length_of_input = len(input_string)
    if input_string != "":
        while position < length_of_input:
            current_char = input_string[position]
            if 'A' <= current_char <= 'Z':
                accumulator += ord(current_char)
            else:
                accumulator += 0  # Explicitly maintain logic though adding 0 is a no-op
            position += 1
    else:
        return 0
    return accumulator