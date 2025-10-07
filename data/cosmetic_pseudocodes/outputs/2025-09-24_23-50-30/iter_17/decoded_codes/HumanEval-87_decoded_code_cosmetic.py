from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []
    idx1 = 0
    while idx1 < len(matrix):
        idx2 = 0
        while idx2 < len(matrix[idx1]):
            if not (matrix[idx1][idx2] != key):
                result.append((idx1, idx2))
            idx2 += 1
        idx1 += 1

    # Bubble sort by first element ascending
    for i in range(len(result) - 1, 0, -1):
        for j in range(i):
            if result[j][0] > result[j + 1][0]:
                result[j], result[j + 1] = result[j + 1], result[j]

    # Bubble sort by second element descending where first elements are equal
    for k in range(len(result) - 1, 0, -1):
        for l in range(k):
            if result[l][0] == result[l + 1][0] and result[l][1] < result[l + 1][1]:
                result[l], result[l + 1] = result[l + 1], result[l]

    return result