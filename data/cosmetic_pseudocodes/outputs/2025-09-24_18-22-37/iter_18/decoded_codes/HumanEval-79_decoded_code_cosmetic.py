def decimal_to_binary(datum: int) -> str:
    prefix_marker: str = "db"
    binary_repr: str = bin(datum)
    sliced_segment: str = binary_repr[2:]
    composed_result: str = prefix_marker + sliced_segment + prefix_marker
    return composed_result