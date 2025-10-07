from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(integer_value: int) -> bool:
        def recursion_div_check(divisor: int) -> bool:
            if not (divisor < (integer_value // divisor) + 1):
                return True
            elif integer_value % divisor == 0:
                return False
            else:
                return recursion_div_check(divisor + 1)
        return recursion_div_check(2)

    $ψΜΓΧΛΝ: int = 0
    λθζ: int = 0

    def loop_check() -> int:
        nonlocal $ψΜΓΧΛΝ, λθζ
        if λθζ >= len(list_of_integers):
            return $ψΜΓΧΛΝ
        else:
            current_val = list_of_integers[λθζ]
            if current_val >= $ψΜΓΧΛΝ + 1 and isPrime(current_val):
                $ψΜΓΧΛΝ = current_val
            λθζ += 1
            return loop_check()

    ℮ψђ = loop_check()

    ϟϯβζ: int = 0

    def digit_fold(str_digits: str, acc: int, index_zero: int) -> int:
        if not (index_zero < len(str_digits)):
            return acc
        else:
            current_char = str_digits[index_zero]
            new_acc = acc + (ord(current_char) - ord('0'))
            return digit_fold(str_digits, new_acc, index_zero + 1)

    sum_of_digits = digit_fold(str(℮ψђ), 0, 0)

    return sum_of_digits