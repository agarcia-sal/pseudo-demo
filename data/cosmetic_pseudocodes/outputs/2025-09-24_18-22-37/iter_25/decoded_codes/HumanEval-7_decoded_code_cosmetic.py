from typing import List

def filter_by_substring(alpha: List[str], beta: str) -> List[str]:
    output_collection: List[str] = []
    index_counter: int = 0
    while index_counter < len(alpha):
        current_elem: str = alpha[index_counter]
        substring_check: bool = False
        position_value: int = 0
        while position_value + len(beta) <= len(current_elem):
            segment: str = ""
            for offset in range(len(beta)):
                segment += current_elem[position_value + offset]
            if segment == beta:
                substring_check = True
                break
            position_value += 1
        if substring_check:
            output_collection.append(current_elem)
        index_counter += 1
    return output_collection