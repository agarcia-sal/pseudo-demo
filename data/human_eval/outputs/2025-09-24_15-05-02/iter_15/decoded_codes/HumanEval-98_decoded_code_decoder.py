def count_upper(input_string: str) -> int:
    count = 0
    for index in range(0, len(input_string), 2):
        if input_string[index] in "AEIOU":
            count += 1
    return count