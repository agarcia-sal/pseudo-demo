from typing import List, Any

def common(arrayA: List[Any], arrayB: List[Any]) -> List[Any]:
    result: dict[Any, bool] = {}
    for indexA in range(len(arrayA)):
        for indexB in range(len(arrayB)):
            if arrayA[indexA] == arrayB[indexB]:
                result[arrayA[indexA]] = True
            else:
                continue
    return sorted(result.keys())