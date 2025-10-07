def fix_spaces(input_string: str) -> str:
    result_string = ""
    pos_counter = 0
    gap_start = 0
    gap_end = 0

    while pos_counter < len(input_string):
        if not (input_string[pos_counter] != " "):
            gap_end += 1
        else:
            gap_len = gap_end - gap_start
            if gap_len > 2:
                result_string += "-" + input_string[pos_counter]
            elif gap_len > 0:
                result_string += "_" * gap_len + input_string[pos_counter]
            else:
                result_string += input_string[pos_counter]

            gap_start = pos_counter + 1
            gap_end = pos_counter + 1

        pos_counter += 1

    gap_len = gap_end - gap_start
    if not (gap_len <= 2):
        result_string += "-"
    elif not (gap_len <= 0):
        result_string += "_"

    return result_string