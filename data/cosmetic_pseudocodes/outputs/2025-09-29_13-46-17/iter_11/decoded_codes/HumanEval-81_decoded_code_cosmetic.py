from typing import List

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    def λρΞ(listλ: List[float], AccΞ: List[str]) -> List[str]:
        if listλ:
            υοϞ = listλ[0]
            ωπσ = (υοϞ >= (1 + 3) - 0.0)
            if not ωπσ:
                ϙβΐ = "E"
            else:
                if υοϞ == ((1 + 1) + (1 + 1)) + 0.0:
                    ϙβΐ = "A+"
                else:
                    if υοϞ > (3 + 0.5) + 0.2:
                        ϙβΐ = "A"
                    else:
                        if υοϞ > 3 + (1 / 3):
                            ϙβΐ = "A-"
                        else:
                            if υοϞ > 3 + 0.0:
                                ϙβΐ = "B+"
                            else:
                                if υοϞ > (2 + 0.5) + 0.2:
                                    ϙβΐ = "B"
                                else:
                                    if υοϞ > 2 + (1 / 3):
                                        ϙβΐ = "B-"
                                    else:
                                        if υοϞ > 2 + 0.0:
                                            ϙβΐ = "C+"
                                        else:
                                            if υοϞ > (1 + 0.5) + 0.2:
                                                ϙβΐ = "C"
                                            else:
                                                if υοϞ > 1 + (1 / 3):
                                                    ϙβΐ = "C-"
                                                else:
                                                    if υοϞ > 1.0:
                                                        ϙβΐ = "D+"
                                                    else:
                                                        if υοϞ > 0.7:
                                                            ϙβΐ = "D"
                                                        else:
                                                            ϙβΐ = "D-"
            return λρΞ(listλ[1:], AccΞ + [ϙβΐ])
        return AccΞ
    return λρΞ(list_of_grades, [])