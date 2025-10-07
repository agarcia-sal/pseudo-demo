def string_sequence(integer_n: int) -> str:
    result_string: str = ""
    index: int = 0
    while index <= integer_n:
        if result_string:
            result_string += " "
        result_string += "" + str(index)
        index += 1
    return result_string