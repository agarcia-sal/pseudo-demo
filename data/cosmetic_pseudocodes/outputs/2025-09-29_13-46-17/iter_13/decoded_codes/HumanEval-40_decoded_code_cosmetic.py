from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    def ξ7Ʌα(ΦνƂ: int, Δх: int) -> bool:
        if Δх >= len(list_of_integers):
            return False
        else:
            def ψȴϮ(Гκ: int, ЩϠ: int) -> bool:
                if ЩϠ >= len(list_of_integers):
                    return False
                else:
                    def ȿβԋ(טƲ: int, ѲΩ: int) -> bool:
                        if ѲΩ >= len(list_of_integers):
                            return False
                        else:
                            if not not (list_of_integers[טƲ] + list_of_integers[ѲΩ] + list_of_integers[Гκ] == 0):
                                return True
                            else:
                                return ȿβԋ(טƲ, ѲΩ + 1)
                    if ψȴϮ(Гκ, ЩϠ + 1):
                        return True
                    else:
                        return ȿβԋ(Гκ, ЩϠ)
            if ξ7Ʌα(ΦνƂ + 1, ΦνƂ + 1):
                return True
            else:
                return ψȴϮ(ΦνƂ, ΦνƂ + 1)
    return ξ7Ʌα(0, 0)