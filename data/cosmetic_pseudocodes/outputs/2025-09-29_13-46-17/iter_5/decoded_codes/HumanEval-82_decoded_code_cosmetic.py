from typing import Optional


def prime_length(input_string: str) -> bool:
    len_STRING: int = len(input_string)
    isPrimeFlag: bool = True
    if not (len_STRING > 1):
        isPrimeFlag = False
    else:
        divisor_iter: int = 2
        while divisor_iter * divisor_iter <= len_STRING and isPrimeFlag:
            if len_STRING % divisor_iter == 0:
                isPrimeFlag = False
            divisor_iter += 1
    return isPrimeFlag