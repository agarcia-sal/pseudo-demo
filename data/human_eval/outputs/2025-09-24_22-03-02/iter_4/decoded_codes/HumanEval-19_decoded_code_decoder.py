def sort_numbers(numbers: str) -> str:
    value_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    filtered_numbers = [x for x in numbers.split(' ') if x]
    sorted_numbers = sorted(filtered_numbers, key=lambda x: value_map[x])
    return ' '.join(sorted_numbers)