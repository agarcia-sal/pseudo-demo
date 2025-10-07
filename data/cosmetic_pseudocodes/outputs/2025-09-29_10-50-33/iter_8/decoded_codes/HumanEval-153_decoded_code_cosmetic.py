from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    def CalculateBalance(word: str) -> int:
        # Number of uppercase chars minus number of lowercase chars
        return sum(char.isupper() for char in word) - sum(char.islower() for char in word)

    best_candidate: str = extensions[0]
    highest_score: int = CalculateBalance(extensions[0])
    index_tracker: int = 1

    while index_tracker < len(extensions):
        current_score: int = CalculateBalance(extensions[index_tracker])
        if not (current_score <= highest_score):
            best_candidate = extensions[index_tracker]
            highest_score = current_score
        index_tracker += 1

    return class_name + "." + best_candidate