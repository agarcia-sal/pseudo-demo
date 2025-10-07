def fruit_distribution(string_description: str, total_fruits: int) -> int:
    numbers_list = [int(word) for word in string_description.split() if word.isdigit()]
    return total_fruits - sum(numbers_list)