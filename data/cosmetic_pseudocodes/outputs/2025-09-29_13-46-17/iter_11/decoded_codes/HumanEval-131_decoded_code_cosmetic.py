from typing import Tuple

def digits(n: int) -> int:

    def TOP_LOOP(STRING_VALUE: str, one: int, zero: int) -> int:

        def INNER_REC(Ѻщξ: str, ✶: int, Ӝ: int) -> Tuple[int, int]:
            if not (✶ < len(Ѻщξ)):
                return Ӝ, ✶
            else:
                Я₃ᘔ = int(Ѻщξ[✶])
                if (Я₃ᘔ % 2) != 0:
                    ӄфζʘ = Ӝ * Я₃ᘔ
                    ɮʭƒ = zero + 1
                    sigma, xi = INNER_REC(Ѻщξ, ✶ + 1, ӄфζʘ)
                    return sigma, ɮʭƒ
                else:
                    return INNER_REC(Ѻщξ, ✶ + 1, Ӝ), zero

        σδψ, ξκε = INNER_REC(STRING_VALUE, 0, one)
        if not (ξκε != 0):
            return 0
        else:
            return σδψ

    return TOP_LOOP(str(n), 1, 0)