from typing import List


def select_words(parameter_q: str, parameter_z: int) -> List[str]:
    variable_r: List[str] = []
    variable_t: int = 0

    variable_k: int = 0
    while variable_k < len(parameter_q):
        if parameter_q[variable_k] == " ":
            variable_t += 1
        variable_k += 1

    variable_u: int = 0
    variable_v: int = 0

    while True:  # start_iteration
        if variable_u > variable_t:
            return variable_r

        variable_p: int = 0
        variable_m: int = parameter_z

        variable_w: str = ""

        # extract_word
        while True:
            if variable_v >= len(parameter_q):
                break

            if parameter_q[variable_v] == " ":
                variable_w = parameter_q[variable_p:variable_v]
                variable_p = variable_v + 1
                variable_v = variable_p
                break

            variable_v += 1

        else:  # If while exhausted without break, set variable_w to last word
            variable_w = parameter_q[variable_p: variable_v]

        if variable_w == "" and variable_v >= len(parameter_q):
            # Last word was empty (possible if string ends with space), jump to end loop
            return variable_r

        # Count consonants in variable_w
        variable_x: int = 0
        variable_y: int = 0
        vowels = {"a", "e", "i", "o", "u"}

        while variable_x < len(variable_w):
            variable_i = variable_w[variable_x].lower()
            if variable_i not in vowels:
                variable_y += 1
            variable_x += 1

        if variable_y == variable_m:
            variable_r.append(variable_w)

        variable_u += 1