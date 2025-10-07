from typing import List

def all_prefixes(str_arg: str) -> List[str]:
    result_accumulation: List[str] = []
    counter: int = 0
    while counter < len(str_arg):
        result_accumulation.append(str_arg[0 : counter + 1])
        counter += 1
    return result_accumulation