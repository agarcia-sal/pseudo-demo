def fix_spaces(input_string: str) -> str:
    reconstructed_string = ""
    cursor = 0
    gap_start = 0
    gap_limit = 0

    while cursor < len(input_string):
        if input_string[cursor] == " ":
            gap_limit += 1
        else:
            gap_length = gap_limit - gap_start
            if gap_length > 2:
                reconstructed_string += "-" + input_string[cursor]
            elif gap_length > 0:
                reconstructed_string += "_" * gap_length + input_string[cursor]
            else:
                reconstructed_string += input_string[cursor]
            gap_start = cursor + 1
            gap_limit = cursor + 1
        cursor += 1

    gap_length = gap_limit - gap_start
    if gap_length > 2:
        reconstructed_string += "-"
    elif gap_length > 0:
        reconstructed_string += "_"

    return reconstructed_string