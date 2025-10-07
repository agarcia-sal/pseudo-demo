from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    dominant_extension = extensions[0]
    score_dominant = sum(c.isupper() for c in dominant_extension) - sum(c.islower() for c in dominant_extension)

    for candidate_extension in extensions[1:]:
        score_candidate = sum(ch.isupper() for ch in candidate_extension) - sum(ch.islower() for ch in candidate_extension)
        if score_candidate > score_dominant:
            dominant_extension = candidate_extension
            score_dominant = score_candidate

    final_result = class_name + '.' + dominant_extension
    return final_result