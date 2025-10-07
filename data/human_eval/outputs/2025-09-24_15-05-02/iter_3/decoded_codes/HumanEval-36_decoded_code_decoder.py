def fizz_buzz(n: int) -> int:
    # Collect numbers divisible by 11 or 13 within range [0, n)
    divisible_numbers = [i for i in range(n) if i % 11 == 0 or i % 13 == 0]

    # Concatenate string representations of these numbers
    concatenated_str = ''.join(str(num) for num in divisible_numbers)

    # Count how many times '7' appears in the concatenated string
    seven_count = concatenated_str.count('7')

    return seven_count