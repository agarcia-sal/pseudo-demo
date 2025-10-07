from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    letter_result_collection: List[str] = []
    index_tracker: int = 0

    while index_tracker < len(list_of_grades):
        current_gpa: float = list_of_grades[index_tracker]

        if current_gpa == 4.0:
            letter_to_add = "A+"
        else:
            if current_gpa > 3.7:
                letter_to_add = "A"
            else:
                if current_gpa > 3.3:
                    letter_to_add = "A-"
                else:
                    if current_gpa > 3.0:
                        letter_to_add = "B+"
                    else:
                        if current_gpa > 2.7:
                            letter_to_add = "B"
                        else:
                            if current_gpa > 2.3:
                                letter_to_add = "B-"
                            else:
                                if current_gpa > 2.0:
                                    letter_to_add = "C+"
                                else:
                                    if current_gpa > 1.7:
                                        letter_to_add = "C"
                                    else:
                                        if current_gpa > 1.3:
                                            letter_to_add = "C-"
                                        else:
                                            if current_gpa > 1.0:
                                                letter_to_add = "D+"
                                            else:
                                                if current_gpa > 0.7:
                                                    letter_to_add = "D"
                                                else:
                                                    if current_gpa > 0.0:
                                                        letter_to_add = "D-"
                                                    else:
                                                        letter_to_add = "E"

        letter_result_collection.append(letter_to_add)
        index_tracker += 1

    return letter_result_collection