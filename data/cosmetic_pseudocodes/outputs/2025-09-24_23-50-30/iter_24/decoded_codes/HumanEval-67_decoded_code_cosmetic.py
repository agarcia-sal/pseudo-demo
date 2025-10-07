from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    bag: List[int] = []

    tokens: List[str] = string_description.split(" ")

    def accumulate_numbers(index: int) -> None:
        if index >= len(tokens):
            return
        word = tokens[index]
        if word.isdigit():
            bag.append(int(word))
        accumulate_numbers(index + 1)

    accumulate_numbers(0)

    total_collected: int = sum(bag)
    return total_number_of_fruits - total_collected