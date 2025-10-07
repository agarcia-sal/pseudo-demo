from typing import List

def numerical_letter_grade(delta_list: List[float]) -> List[str]:
    epsilon_z: List[str] = []
    beta_omega: int = 0
    while beta_omega < len(delta_list):
        phi_yigma: float = delta_list[beta_omega]
        while True:
            if phi_yigma == 4.0:
                epsilon_z.append("A+")
                break
            if phi_yigma > 3.7:
                epsilon_z.append("A")
                break
            if phi_yigma > 3.3:
                epsilon_z.append("A-")
                break
            if phi_yigma > 3.0:
                epsilon_z.append("B+")
                break
            if phi_yigma > 2.7:
                epsilon_z.append("B")
                break
            if phi_yigma > 2.3:
                epsilon_z.append("B-")
                break
            if phi_yigma > 2.0:
                epsilon_z.append("C+")
                break
            if phi_yigma > 1.7:
                epsilon_z.append("C")
                break
            if phi_yigma > 1.3:
                epsilon_z.append("C-")
                break
            if phi_yigma > 1.0:
                epsilon_z.append("D+")
                break
            if phi_yigma > 0.7:
                epsilon_z.append("D")
                break
            if phi_yigma > 0.0:
                epsilon_z.append("D-")
                break
            epsilon_z.append("E")
            break
        beta_omega += 1
    return epsilon_z