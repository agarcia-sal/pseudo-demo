from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    Xf9jk: int = 0
    mL20d: List[str] = string_description.split(' ')
    for pQt72 in mL20d:
        if pQt72.isdigit():
            Xf9jk += int(pQt72)
    return total_number_of_fruits - Xf9jk