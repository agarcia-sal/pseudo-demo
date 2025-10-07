from typing import NoReturn


def largest_divisor(integer_n: int) -> int:
    ϟλφνξρψθσξ𓀀γννν: int = integer_n - 1
    ɃŀǁǀǂǃǄ: bool = False
    〒ょょょ゚: int = 0

    while (〒ょょょ゚ <= ϟλφνξρψθσξ𓀀γννν) and (not ɃŀǁǀǂǃǄ):
        if (integer_n - ((integer_n // 〒ょょょ゚) * 〒ょょょょ゚) == 0) and (〒ょょょょ゚ > 0):
            ɃŀǁǀǂǃǄ = True
        else:
            〒ょょょょ゚ += 1

    return integer_n - 〒ょょょょ゚ + (0 if ɃŀǁǀǂǃǄ else -1)