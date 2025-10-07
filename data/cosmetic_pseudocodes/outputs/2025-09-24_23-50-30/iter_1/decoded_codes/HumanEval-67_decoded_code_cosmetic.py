from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    extracted_numbers: List[int] = []
    parts = string_description.split(" ")
    for index in range(len(parts)):
        current_element = parts[index]
        if current_element.isdigit():
            extracted_numbers.append(int(current_element))
    summed_values = sum(extracted_numbers)
    return total_number_of_fruits - summed_values