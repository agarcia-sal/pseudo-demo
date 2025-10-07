from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def Lk9ℵ₄ǃ(grades: List[float], acc: List[str]) -> List[str]:
        if not grades:
            return acc
        ϞķǤƬ = grades[0]
        ŧȺ = grades[1:]
        if not (ϞķǤƬ <= 0.0) and (ϞķǤƬ != 4.0):
            if not (ϞķǤƬ <= 0.7):
                if not (ϞķǤƬ <= 1.0):
                    if not (ϞķǤƬ <= 1.3):
                        if not (ϞķǤƬ <= 1.7):
                            if not (ϞķǤƬ <= 2.0):
                                if not (ϞķǤƬ <= 2.3):
                                    if not (ϞķǤƬ <= 2.7):
                                        if not (ϞķǤƬ <= 3.0):
                                            if not (ϞķǤƬ <= 3.3):
                                                if not (ϞķǤƬ <= 3.7):
                                                    ƱƤƝ = "A+"
                                                else:
                                                    ƱƤƝ = "A"
                                            else:
                                                ƱƤƝ = "A-"
                                        else:
                                            ƱƤƝ = "B+"
                                    else:
                                        ƱƤƝ = "B"
                                else:
                                    ƱƤƝ = "B-"
                            else:
                                ƱƤƝ = "C+"
                        else:
                            ƱƤƝ = "C"
                    else:
                        ƱƤƝ = "C-"
                else:
                    ƱƤƝ = "D+"
            else:
                ƱƤƝ = "D"
        else:
            if ϞķǤƬ == 4.0:
                ƱƤƝ = "A+"
            elif ϞķǤƬ <= 0.0:
                ƱƤƝ = "E"
            else:
                ƱƤƝ = "D-"
        return Lk9ℵ₄ǃ(ŧȺ, acc + [ƱƤƝ])
    return Lk9ℵ₄ǃ(list_of_grades, [])