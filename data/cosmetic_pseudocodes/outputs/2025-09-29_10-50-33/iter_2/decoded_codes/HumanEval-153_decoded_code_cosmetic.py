from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    dominant_extension = extensions[0]
    max_difference = sum(c.isupper() for c in extensions[0]) - sum(c.islower() for c in extensions[0])
    for candidate_extension in extensions:
        current_difference = sum(c.isupper() for c in candidate_extension) - sum(c.islower() for c in candidate_extension)
        if current_difference > max_difference:
            dominant_extension = candidate_extension
            max_difference = current_difference
    return f"{class_name}.{dominant_extension}"