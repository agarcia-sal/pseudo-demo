from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    champion = extensions[0]
    champion_score = sum(1 for u in champion if u.isupper()) - sum(1 for l in champion if l.islower())
    idx = 0
    while idx < len(extensions):
        contender = extensions[idx]
        contender_score = 0
        for ch in contender:
            if ch.isupper():
                contender_score += 1
            elif ch.islower():
                contender_score -= 1
        if contender_score > champion_score:
            champion = contender
            champion_score = contender_score
        idx += 1
    return class_name + "." + champion