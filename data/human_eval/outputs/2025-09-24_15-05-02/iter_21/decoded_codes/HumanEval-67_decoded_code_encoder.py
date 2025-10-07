from typing import List

def fruit_distribution(string_description: str, total_fruits: int) -> int:
    numbers_list: List[int] = []
    for word in string_description.split():
        if word.isdigit():
            numbers_list.append(int(word))
    total_apples_and_oranges: int = sum(numbers_list)
    return total_fruits - total_apples_and_oranges