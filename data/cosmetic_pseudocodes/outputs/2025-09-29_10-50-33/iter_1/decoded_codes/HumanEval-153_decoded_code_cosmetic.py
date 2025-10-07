from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    strong: str = extensions[0]
    highest_score: int = 0
    first_str: str = extensions[0]

    upper_count: int = 0
    lower_count: int = 0
    for ch in first_str:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
    highest_score = upper_count - lower_count

    for ext in extensions:
        up = 0
        low = 0
        for c in ext:
            if c.isupper():
                up += 1
            elif c.islower():
                low += 1
        score = up - low
        if score > highest_score:
            strong = ext
            highest_score = score

    return class_name + "." + strong