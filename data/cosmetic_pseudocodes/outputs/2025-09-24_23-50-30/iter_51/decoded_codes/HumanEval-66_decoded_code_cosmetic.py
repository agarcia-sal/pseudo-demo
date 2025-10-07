from typing import List


def digitSum(parameter_alpha: str) -> int:
    if parameter_alpha == "":
        return 0
    else:
        helper_list_gamma: List[int] = list(range(len(parameter_alpha)))

        def recursive_accumulate(list_delta: List[int], acc_epsilon: int) -> int:
            if not list_delta:
                return acc_epsilon
            else:
                head_phi = list_delta[0]
                tail_chi = list_delta[1:]
                char_psi = parameter_alpha[head_phi]
                is_upper = "A" <= char_psi <= "Z"
                addition_val = (is_upper) * ord(char_psi)
                return recursive_accumulate(tail_chi, acc_epsilon + addition_val)

        return recursive_accumulate(helper_list_gamma, 0)