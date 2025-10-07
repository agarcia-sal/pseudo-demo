from typing import List

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    container: List[int] = []
    segments: List[str] = string_description.split(" ")
    for segment in segments:
        if segment.isdigit():
            container.append(int(segment))
    aggregate: int = sum(container)
    return total_number_of_fruits - aggregate