def string_xor(string_a: str, string_b: str) -> str:
    accumulator_string = []
    index_counter = 0
    length_a = len(string_a)
    length_b = len(string_b)

    while index_counter < length_a and index_counter < length_b:
        accumulator_string.append(
            "1" if string_a[index_counter] != string_b[index_counter] else "0"
        )
        index_counter += 1

    return "".join(accumulator_string)