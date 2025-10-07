def even_odd_count(integer_number: int) -> tuple[int, int]:
    even_count = 0
    odd_count = 0
    for character_digit in str(abs(integer_number)):
        if int(character_digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count