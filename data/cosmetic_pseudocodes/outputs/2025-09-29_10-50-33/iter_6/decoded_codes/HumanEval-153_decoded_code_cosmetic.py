import re
from typing import List


def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    def Evaluate_Significance(token: str) -> int:
        uppercase_chars = [c for c in token if re.match(r"[A-Z]", c)]
        lowercase_chars = [c for c in token if re.match(r"[a-z]", c)]
        return len(uppercase_chars) - len(lowercase_chars)

    peak_extension = extensions[0]
    peak_score = Evaluate_Significance(peak_extension)

    def Scan_List(index: int) -> None:
        if index >= len(extensions):
            return
        candidate = extensions[index]
        candidate_score = Evaluate_Significance(candidate)
        if candidate_score > peak_score:
            nonlocal peak_extension, peak_score
            peak_extension = candidate
            peak_score = candidate_score
        Scan_List(index + 1)

    Scan_List(1)

    return f"{class_name}.{peak_extension}"