def even_odd_count(integer_number: int) -> tuple[int, int]:
    tally_even = 0
    tally_odd = 0
    index_cursor = 0
    digit_sequence = str(abs(integer_number))
    while index_cursor < len(digit_sequence):
        current_element = digit_sequence[index_cursor]
        if int(current_element) % 2 == 0:
            tally_even += 1
        else:
            tally_odd += 1
        index_cursor += 1
    return tally_even, tally_odd