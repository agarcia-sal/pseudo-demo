from typing import List

def all_prefixes(given_text: str) -> List[str]:
    accumulation: List[str] = ["" for _ in range(len(given_text))]
    counter: int = 0
    while counter < len(given_text):
        segment: str = given_text[:counter + 1]
        accumulation[counter] = segment
        counter += 1
    return accumulation