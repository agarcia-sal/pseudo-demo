from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    dominant_candidate: str = extensions[0]
    strength_metric: int = sum(ch.isupper() for ch in dominant_candidate) - sum(ch.islower() for ch in dominant_candidate)
    for current_extension in extensions:
        current_metric: int = sum(ch.isupper() for ch in current_extension) - sum(ch.islower() for ch in current_extension)
        if current_metric > strength_metric:
            dominant_candidate = current_extension
            strength_metric = current_metric
    final_output: str = class_name + "." + dominant_candidate
    return final_output