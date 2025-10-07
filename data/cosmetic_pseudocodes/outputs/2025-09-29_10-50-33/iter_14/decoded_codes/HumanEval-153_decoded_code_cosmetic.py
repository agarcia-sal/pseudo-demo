from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    def assess_strength(extension_text: str, accumulator: int) -> int:
        if accumulator >= 1:
            upper_count = sum('A' <= ch <= 'Z' for ch in extension_text)
            lower_count = sum('a' <= ch <= 'z' for ch in extension_text)
            return upper_count - lower_count
        else:
            return 0

    current_strongest = extensions[0]
    current_strength = assess_strength(extensions[0], 1)

    iterator_index = 0
    while iterator_index < len(extensions):
        candidate_extension = extensions[iterator_index]
        candidate_strength = assess_strength(candidate_extension, 1)

        if candidate_strength > current_strength:  # NOT candidate_strength <= current_strength
            current_strongest = candidate_extension
            current_strength = candidate_strength

        iterator_index += 1

    composed_result = f"{class_name}.{current_strongest}"
    return composed_result