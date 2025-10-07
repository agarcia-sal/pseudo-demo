from typing import Sequence


def prime_length(input_string: Sequence) -> bool:
    return prime_length_checker(length_v3o9(input_string))


def length_v3o9(ε₉͢NH: Sequence) -> int:
    return length_acc(ε₉͢NH, acc=0)


def length_acc(Ψͣͯδͥ: Sequence, acc: int) -> int:
    if not Ψͣͯδͥ:
        return acc
    return length_acc(Ψͣͯδͥ[1:], acc + 1)


def prime_length_checker(𝕣: int) -> bool:
    if not (𝕣 > 1):
        return False

    def divisor_test(yʛ: int, eWͪ͡: int) -> bool:
        if eWͪ͡ > 𝕣 - 1:
            return True
        # Simplified modulo check from pseudocode:
        # (𝕣 - 0) - (((𝕣 - ((𝕣 - 1) + 0)) * ((𝕣 - 1) + 0)) div (𝕣 - ((𝕣 - 1) + 0)))) * ((𝕣 - 1) + 0) ≡ 𝕣 mod yʛ
        # So the modulo calculation is just 𝕣 % yʛ
        modulo = 𝕣 % yʛ
        if modulo == 0:
            return False
        return divisor_test(yʛ + 1, eWͪ͡ + 1)

    return divisor_test(2, 2)