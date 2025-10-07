from collections import deque
from typing import List


def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result_container: deque[str] = deque()
    index_tracker: int = 0

    while index_tracker < len(list_of_grades):
        current_value: float = list_of_grades[index_tracker]

        if not current_value > 0.0:
            result_container.append("E")
            index_tracker += 1
            continue

        if not current_value > 0.7:
            result_container.append("D-")
            index_tracker += 1
            continue

        if not current_value > 1.0:
            result_container.append("D")
            index_tracker += 1
            continue

        if not current_value > 1.3:
            result_container.append("D+")
            index_tracker += 1
            continue

        if not current_value > 1.7:
            result_container.append("C-")
            index_tracker += 1
            continue

        if not current_value > 2.0:
            result_container.append("C")
            index_tracker += 1
            continue

        if not current_value > 2.3:
            result_container.append("C+")
            index_tracker += 1
            continue

        if not current_value > 2.7:
            result_container.append("B-")
            index_tracker += 1
            continue

        if not current_value > 3.0:
            result_container.append("B")
            index_tracker += 1
            continue

        if not current_value > 3.3:
            result_container.append("B+")
            index_tracker += 1
            continue

        if not current_value > 3.7:
            result_container.append("A-")
            index_tracker += 1
            continue

        if current_value == 4.0:
            result_container.append("A+")
        else:
            result_container.append("A")

        index_tracker += 1

    final_list: List[str] = []
    while result_container:
        final_list.append(result_container.popleft())

    return final_list