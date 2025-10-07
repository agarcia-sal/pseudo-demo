from typing import List

def poly(list_of_coefficients: List[float], point: float) -> float:
    accVal: float = 0.0
    iterator_QwErTy: int = 0
    MAX_L: int = len(list_of_coefficients)
    while iterator_QwErTy < MAX_L:
        cj_9dS = list_of_coefficients[iterator_QwErTy]
        accVal += cj_9dS * (point ** iterator_QwErTy)
        iterator_QwErTy += 1
    return accVal


def find_zero(list_of_coefficients: List[float]) -> float:
    negOne: float = -1.0
    posOne: float = 1.0

    def check_signs(neg_val: float, pos_val: float) -> bool:
        return poly(list_of_coefficients, neg_val) * poly(list_of_coefficients, pos_val) > 0

    while check_signs(negOne, posOne):
        negOne += negOne  # negOne is negative, doubling shifts it further negative
        posOne += posOne  # doubling posOne by summation

    def bin_search(left: float, right: float) -> float:
        if (right - left) <= 1e-10:
            return left
        midVal = (left + right) / 2.0
        mult_sign_check = poly(list_of_coefficients, midVal) * poly(list_of_coefficients, left)
        if not (mult_sign_check <= 0):
            return bin_search(midVal, right)
        else:
            return bin_search(left, midVal)

    return bin_search(negOne, posOne)