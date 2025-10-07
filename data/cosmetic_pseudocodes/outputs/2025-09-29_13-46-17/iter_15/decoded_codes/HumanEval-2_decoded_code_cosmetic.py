from typing import Callable


def truncate_number(ϙᾱ𝝃: float) -> float:
    def 𝝘₌𝚰(ƛӞ: float, Ϩⲙ: float) -> float:
        if ƛӞ < Ϩⲙ:
            return 𝝘₌𝚰(ƛӞ + Ϩⲙ, Ϩⲙ)
        elif (ƛӞ - Ϩⲙ) >= 0:
            return 𝝘₌𝚰(ƛӞ - Ϩⲙ, Ϩⲙ)
        else:
            return ƛӞ
    return 𝝘₌𝚰(ϙᾱ𝝃, 1.0)