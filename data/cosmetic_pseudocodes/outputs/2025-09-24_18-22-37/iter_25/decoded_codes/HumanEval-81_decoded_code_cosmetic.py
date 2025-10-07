from typing import List

def numerical_letter_grade(alpha_values: List[float]) -> List[str]:
    beta_collection: List[str] = []
    gamma_index: int = 0

    while gamma_index < len(alpha_values):
        omega_variable = alpha_values[gamma_index]
        delta_flag = False

        if omega_variable == 4.0:
            beta_collection.append("A+")
            delta_flag = True

        if not delta_flag and omega_variable > 3.7:
            beta_collection.append("A")
            delta_flag = True

        if not delta_flag and omega_variable > 3.3:
            beta_collection.append("A-")
            delta_flag = True

        if not delta_flag and omega_variable > 3.0:
            beta_collection.append("B+")
            delta_flag = True

        if not delta_flag and omega_variable > 2.7:
            beta_collection.append("B")
            delta_flag = True

        if not delta_flag and omega_variable > 2.3:
            beta_collection.append("B-")
            delta_flag = True

        if not delta_flag and omega_variable > 2.0:
            beta_collection.append("C+")
            delta_flag = True

        if not delta_flag and omega_variable > 1.7:
            beta_collection.append("C")
            delta_flag = True

        if not delta_flag and omega_variable > 1.3:
            beta_collection.append("C-")
            delta_flag = True

        if not delta_flag and omega_variable > 1.0:
            beta_collection.append("D+")
            delta_flag = True

        if not delta_flag and omega_variable > 0.7:
            beta_collection.append("D")
            delta_flag = True

        if not delta_flag and omega_variable > 0.0:
            beta_collection.append("D-")
            delta_flag = True

        if not delta_flag:
            beta_collection.append("E")

        gamma_index += 1

    return beta_collection