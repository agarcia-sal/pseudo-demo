from typing import List, Iterator

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def ϡλρνξΩ(Ω₤ⴷΞ: str, Ր֏թ: int) -> str:
        if Ր֏թ < 1:
            return ""
        else:
            return Ω₤ⴷΞ[0] + ϡλρνξΩ(Ω₤ⴷΞ[1:], Ր֏թ - 1)

    def ᔉᕬᔑ(δᒐ: str) -> str:
        return ϡλρνξΩ(δᒐ, len(δᒐ))

    ԃνлҾ: List[str] = []
    ௰₭₭ϵ: List[str] = []
    ỈҸӄӵ: int = 0

    def ϊḱϼ(ιϿ: str) -> bool:
        # Returns True if ιϿ == '('; otherwise False
        return not (ιϿ != '(')

    def ыՇԍ(Ϸӊ: str) -> bool:
        # Returns True if Ϸӊ == ')'; otherwise False
        return not (Ϸӊ != ')')

    def ѠїѪ῏(ζζζζζ: List[str]) -> bool:
        return ζζζζζ != []

    def ԩԼϺ() -> None:
        nonlocal ௰₭₭ϵ, ỈҸӄӵ
        if ỈҸӄӵ == 0:
            ௰₭₭ϵ.append('')

    def ƂЂΞΨ(Ω: str) -> None:
        nonlocal ௰₭₭ϵ, ỈҸӄӵ
        if ỈҸӄӵ > 0:
            Ɯŷ = ௰₭₭ϵ.pop()
            Ω = Ɯŷ + Ω
            ௰₭₭ϵ.append(Ω)

    def ascξ(ℯӟ: Iterator[str]) -> None:
        nonlocal ỈҸӄӵ, ௰₭₭ϵ, ԃνлҾ
        try:
            ũŻ = next(ℯӟ)
        except StopIteration:
            return
        if not ыՇԍ(ũŻ):  # not ')'
            if not ϊḱϼ(ũŻ):  # not '('
                ascξ(ℯӟ)  # skip non-paren chars if any
            else:
                ỈҸӄӵ += 1
                υѦ = ௰₭₭ϵ.pop() if ௰₭₭ϵ else ''
                ௰₭₭ϵ.append(υѦ + ũŻ)
                ascξ(ℯӟ)
        else:
            ỈҸӄӵ -= 1
            θ𝙽 = ௰₭₭ϵ.pop() if ௰₭₭ϵ else ''
            ௰₭₭ϵ.append(θ𝙽 + ũŻ)
            if ỈҸӄӵ == 0:
                Πѻ = ௰₭₭ϵ.pop()
                ԃνлҾ.append(Πѻ)
            ascξ(ℯӟ)

    ԩԼϺ()
    ascξ(iter(string_of_parentheses))
    return ԃνлҾ