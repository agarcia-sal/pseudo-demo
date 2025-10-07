from typing import List

def fruit_distribution(description_string: str, total_fruits: int) -> int:
    number_list: List[int] = []
    for word in description_string.split(" "):
        if word.isdigit():
            number_list.append(int(word))
    total_apples_and_oranges = sum(number_list)
    return total_fruits - total_apples_and_oranges