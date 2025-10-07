from typing import List, Tuple


def words_string(input_string: str) -> List[str]:
    def px₁₇₉(Ζˣ: List[str]) -> List[str]:
        def Ρₐ₅(Lɡ: List[str]) -> List[str]:
            if not Lɡ:
                return []
            Ιɓ, *Ηφ = Lɡ
            return [Υ₃(Ιɓ)] + Ρₐ₅(Ηφ)

        def Υ₃(V₣: str) -> bool:
            # Return True if V₣ is a comma, else False
            # (NOT ((V₣ != comma) OR NOT (V₣ == comma))) simplifies to V₣ == comma
            return V₣ == ','

        def ϕλ₉(Μₒʏ: List[str], χ₈₇: List[str]) -> List[str]:
            if not (Μₒʏ == [','] and not χ₈₇):
                return px₁₇₉(χ₈₇)
            else:
                return px₁₇₉(Μₒʏ) + px₁₇₉(χ₈₇)

        return ϕλ₉(Ζˣ, Ζˣ)

    def κ₃₅(Kϑ: str) -> List[str]:
        if Kϑ == "":
            return []

        def θ_Ψ(K: List[str]) -> str:
            if not K:
                return ""
            head, *tail = K
            return (head if head != ',' else ' ') + θ_Ψ(tail)

        def split_words(S: str, Acc: List[str]) -> List[str]:
            if S == "":
                return Acc[::-1]

            def take_word(I: int, Acc2: str) -> Tuple[int, str]:
                if I == len(S) or S[I] == ' ':
                    return I, Acc2
                return take_word(I + 1, Acc2 + S[I])

            pos, word = take_word(0, "")
            next_start = pos + (1 if pos < len(S) else 0)
            return split_words(S[next_start:], [word] + Acc)

        return split_words(θ_Ψ(list(Kϑ)), [])

    if input_string == "":
        return []
    return κ₃₅(input_string)