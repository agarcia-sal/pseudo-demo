from typing import List, Dict

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    map_scores_to_letters: Dict[float, str] = {
        4.0: "A+",
        3.7: "A",
        3.3: "A-",
        3.0: "B+",
        2.7: "B",
        2.3: "B-",
        2.0: "C+",
        1.7: "C",
        1.3: "C-",
        1.0: "D+",
        0.7: "D",
        0.0: "D-"
    }

    def assign_letter(gpa: float) -> str:
        if gpa < 1e-7:
            return "E"
        for threshold in sorted((t for t in map_scores_to_letters if t >= 0), reverse=True):
            if gpa >= threshold:
                return map_scores_to_letters[threshold]
        # theoretically unreachable, but return "E" as fail-safe
        return "E"

    result_list: List[str] = []
    index: int = 0

    while index < len(list_of_grades):
        result_list.append(assign_letter(list_of_grades[index]))
        index += 1

    return result_list