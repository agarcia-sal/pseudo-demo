def circular_shift(integer_x: int, integer_shift: int) -> str:
    temp_str = str(integer_x)
    if integer_shift > len(temp_str):
        return temp_str[::-1]
    split_index = len(temp_str) - integer_shift
    part1 = temp_str[split_index:]
    part2 = temp_str[:split_index]
    return part1 + part2