from typing import List, Any

def intersperse(numbers: List[Any], delimeter: Any) -> List[Any]:
    if not numbers:
        return []
    result: List[Any] = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)
    result.append(numbers[-1])
    return result