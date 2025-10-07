def fix_spaces(text: str) -> str:
    result_text: str = ""
    current_index: int = 0
    gap_start: int = 0
    gap_end: int = 0

    while current_index < len(text):
        if text[current_index] != " ":
            gap_length = gap_end - gap_start
            if gap_length > 2:
                result_text += "-" + text[current_index]
            else:
                if gap_length > 0:
                    result_text += "_" * gap_length + text[current_index]
                else:
                    result_text += text[current_index]
            gap_end = current_index + 1
            gap_start = current_index + 1
        else:
            gap_end += 1
        current_index += 1

    trailing_gap_length = gap_end - gap_start
    if trailing_gap_length > 2:
        result_text += "-"
    elif trailing_gap_length > 0:
        result_text += "_"

    return result_text