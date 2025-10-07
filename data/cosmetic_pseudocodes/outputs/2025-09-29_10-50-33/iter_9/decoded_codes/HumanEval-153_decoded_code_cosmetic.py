from typing import List


def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    leader: str = extensions[0]
    dominance_score: int = sum(c.isupper() for c in leader) - sum(c.islower() for c in leader)

    position_tracker: int = 0
    while position_tracker < len(extensions):
        contender: str = extensions[position_tracker]
        contender_score: int = sum(c.isupper() for c in contender) - sum(c.islower() for c in contender)

        if not (contender_score <= dominance_score):
            leader = contender
            dominance_score = contender_score

        position_tracker += 1

    result_identifier: str = f"{class_name}.{leader}"
    return result_identifier