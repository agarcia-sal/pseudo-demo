from typing import List


def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    principal_extension: str = extensions[0]
    principal_metric: int = sum(1 for c in principal_extension if c.isupper()) - sum(1 for c in principal_extension if c.islower())

    cursor: int = 1
    while cursor < len(extensions):
        candidate: str = extensions[cursor]
        candidate_metric: int = 0
        position: int = 0
        while position < len(candidate):
            if candidate[position].isupper():
                candidate_metric += 1
            elif candidate[position].islower():
                candidate_metric -= 1
            position += 1
        if candidate_metric > principal_metric:
            principal_metric = candidate_metric
            principal_extension = candidate
        cursor += 1

    combined_name: str = f"{class_name}.{principal_extension}"
    return combined_name