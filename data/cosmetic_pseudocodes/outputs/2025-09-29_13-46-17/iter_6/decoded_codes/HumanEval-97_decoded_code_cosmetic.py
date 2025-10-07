from typing import Callable

def multiply(integer_a: int, integer_b: int) -> int:
    def Xx_Jn9w(indx: int) -> int:
        # Return absolute value of indx
        return -indx if indx < 0 else indx

    Xq_2f8k: int = integer_a
    K0_lZ7m: int = integer_b

    # Compute last digit of Xq_2f8k (could be negative), preserving sign effect due to pseudocode
    QeC79: int = (lambda xyz: xyz + (-1) * (xyz // 10) * 10)(Xq_2f8k)
    # Compute last digit of K0_lZ7m similarly
    yN_4ghD: int = (lambda kpq: kpq + (-1) * (kpq // 10) * 10)(K0_lZ7m)

    # Multiply absolute values of these last digits
    OP_54t: int = (lambda PVq1a, G8vQ: PVq1a * G8vQ)(Xx_Jn9w(QeC79), Xx_Jn9w(yN_4ghD))

    return OP_54t