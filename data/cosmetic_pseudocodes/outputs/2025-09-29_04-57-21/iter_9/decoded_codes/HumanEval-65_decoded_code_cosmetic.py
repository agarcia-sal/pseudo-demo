def circular_shift(integer_x: int, integer_shift: int) -> str:
    digit_sequence: str = str(integer_x)
    total_length: int = len(digit_sequence)

    if integer_shift > total_length:
        # Reverse the sequence manually
        reversed_sequence = ''
        index = total_length - 1
        while index >= 0:
            reversed_sequence += digit_sequence[index]
            index -= 1
        return reversed_sequence

    split_index = total_length - integer_shift
    tail_part = digit_sequence[split_index:total_length]
    head_part = digit_sequence[0:split_index]
    return tail_part + head_part