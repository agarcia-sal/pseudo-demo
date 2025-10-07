def multiply(number_one: int, number_two: int) -> int:
    first_digit = abs(number_one - (number_one // 10) * 10)
    second_digit = abs(number_two - (number_two // 10) * 10)
    return second_digit * first_digit