def solve(N: int) -> str:
    digits_string = str(N)
    digits_list = []
    index = 0
    while index < len(digits_string):
        current_character = digits_string[index]
        current_digit = int(current_character)
        digits_list.append(current_digit)
        index += 1
    total_sum = 0
    sum_index = 0
    while sum_index < len(digits_list):
        total_sum += digits_list[sum_index]
        sum_index += 1
    binary_representation = bin(total_sum)
    result_string = binary_representation[2:]
    return result_string