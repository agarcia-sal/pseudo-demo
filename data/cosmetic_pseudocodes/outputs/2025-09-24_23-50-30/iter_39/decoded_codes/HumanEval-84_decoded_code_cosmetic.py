from typing import List


def solve(parameter_Omega: int) -> str:
    accumulator_Phi: int = 0
    list_Zeta: List[str] = []
    string_Upsilon: str = str(parameter_Omega)
    index_Rho: int = 0

    while index_Rho < len(string_Upsilon):
        element_Tau: str = string_Upsilon[index_Rho]
        list_Zeta.append(element_Tau)
        index_Rho += 1

    def helper_Sigma(sequence_Alpha: List[str], position_Eta: int, total_Kappa: int) -> int:
        if position_Eta == len(sequence_Alpha):
            return total_Kappa
        digit_Mu: int = int(sequence_Alpha[position_Eta])
        return helper_Sigma(sequence_Alpha, position_Eta + 1, total_Kappa + digit_Mu)

    accumulator_Phi = helper_Sigma(list_Zeta, 0, 0)

    def convert_Binary(delta: int) -> str:
        if delta == 0:
            return '0'
        result_Lambda: str = ''
        while delta > 0:
            remainder_Nu: int = delta % 2
            delta //= 2
            result_Lambda = str(remainder_Nu) + result_Lambda
        return result_Lambda

    binary_String: str = convert_Binary(accumulator_Phi)
    return binary_String