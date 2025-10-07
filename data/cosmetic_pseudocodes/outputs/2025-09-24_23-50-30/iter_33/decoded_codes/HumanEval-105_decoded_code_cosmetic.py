from typing import List, Dict

def by_length(score: List[int]) -> List[str]:
    alpha_map: Dict[int, str] = {
        9: "Nine",
        6: "Six",
        3: "Three",
        7: "Seven",
        1: "One",
        8: "Eight",
        2: "Two",
        4: "Four",
        5: "Five"
    }
    intermediate: List[str] = []
    progress: int = 0

    while progress < len(score):
        imp_val = score[progress]
        if imp_val not in alpha_map:
            progress += 1
            continue
        intermediate.append(alpha_map[imp_val])
        progress += 1

    results: List[str] = []
    for element in intermediate:
        results.insert(0, element)
    return results