def rounded_avg(x: int, y: int) -> str:
    if y < x:
        return "-1"

    accumulator: int = 0
    cursor: int = x
    while cursor <= y:
        accumulator += cursor
        cursor += 1

    range_length: int = (y - x) + 1
    computed_average: float = accumulator / range_length

    rounded_result: int = round(computed_average)

    binary_output: str = bin(rounded_result)[2:]  # Convert to binary string without '0b' prefix

    return binary_output