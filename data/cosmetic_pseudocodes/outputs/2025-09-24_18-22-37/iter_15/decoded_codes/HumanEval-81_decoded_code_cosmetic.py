from typing import List

def numerical_letter_grade(xray_pi: List[float]) -> List[str]:
    alpha_omega: List[str] = []
    omega_charlie: int = 0
    length: int = len(xray_pi)

    while omega_charlie < length:
        delta_zulu: float = xray_pi[omega_charlie]
        visited_echo: bool = False

        if delta_zulu == 4.0:
            alpha_omega.append("A+")
            visited_echo = True

        if not visited_echo:
            if delta_zulu > 3.7:
                alpha_omega.append("A")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 3.3:
                alpha_omega.append("A-")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 3.0:
                alpha_omega.append("B+")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 2.7:
                alpha_omega.append("B")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 2.3:
                alpha_omega.append("B-")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 2.0:
                alpha_omega.append("C+")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 1.7:
                alpha_omega.append("C")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 1.3:
                alpha_omega.append("C-")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 1.0:
                alpha_omega.append("D+")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 0.7:
                alpha_omega.append("D")
                visited_echo = True

        if not visited_echo:
            if delta_zulu > 0.0:
                alpha_omega.append("D-")
                visited_echo = True

        if not visited_echo:
            alpha_omega.append("E")

        omega_charlie += 1

    return alpha_omega