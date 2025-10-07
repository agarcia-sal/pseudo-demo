from typing import List

def concatenate(bucket: List[str]) -> str:
    def helper(index: int, accumulator: str) -> str:
        if not (index < len(bucket)):
            return accumulator
        else:
            return helper(index + 1, accumulator + bucket[index])
    return helper(0, "")