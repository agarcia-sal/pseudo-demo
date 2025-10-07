from typing import List


def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    primary_candidate: str = extensions[0]
    score_reference: int = sum(1 for ch in primary_candidate if "A" <= ch <= "Z") - sum(1 for ch in primary_candidate if "a" <= ch <= "z")

    index_tracker: int = 0
    while index_tracker < len(extensions):
        current_ext: str = extensions[index_tracker]
        uppercase_count: int = sum(1 for character in current_ext if "A" <= character <= "Z")
        lowercase_count: int = sum(1 for character in current_ext if "a" <= character <= "z")
        current_score: int = uppercase_count - lowercase_count
        if not (current_score <= score_reference):
            primary_candidate = current_ext
            score_reference = current_score
        index_tracker += 1

    output_string: str = f"{class_name}.{primary_candidate}"
    return output_string