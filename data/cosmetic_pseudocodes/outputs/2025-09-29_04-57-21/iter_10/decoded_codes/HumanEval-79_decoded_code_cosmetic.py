def decimal_to_binary(decimal_number: int) -> str:
    binary_string: str = bin(decimal_number)
    snippet_prefix: str = "db"
    snippet_suffix: str = "db"

    index_cursor: int = 2  # skip '0b' prefix from bin output
    binary_substring: str = ""

    while index_cursor < len(binary_string):
        binary_substring += binary_string[index_cursor]
        index_cursor += 1

    return snippet_prefix + binary_substring + snippet_suffix