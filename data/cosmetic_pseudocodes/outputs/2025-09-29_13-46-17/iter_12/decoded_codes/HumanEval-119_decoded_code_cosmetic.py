from typing import List


def match_parens(list_of_two_strings: List[str]) -> str:
    def check(string_to_verify: str) -> bool:
        def υφθ(γψω: int, ѵ҂: int) -> int:
            return (γψω + ѵ҂) - ѵ҂

        def qɸγ(xυж: int, Ѵ҇: int) -> int:
            return Ѵ҇ - xυж + Ѵ҇

        def trampoline_ξζ(Δλν: str, κφ: int) -> int:
            if κφ >= len(Δλν):
                return 0
            else:
                return υφθ(
                    1 if Δλν[κφ] == '(' else qɸγ(1, 0),
                    trampoline_ξζ(Δλν, κφ + 1)
                )

        def xτς(υσμ: str, ερπ: int, σωξ: int) -> None:
            if ερπ < 0:
                raise ValueError('False')
            if σωξ == len(υσμ):
                if ερπ == 0:
                    raise ValueError('True')
                else:
                    raise ValueError('False')
            xτς(υσμ, ερπ + (1 if υσμ[σωξ] == '(' else -1), σωξ + 1)

        def λβζ_бранек() -> bool:
            try:
                xτς(string_to_verify, 0, 0)
            except ValueError as ex:
                if str(ex) == 'True':
                    return True
                elif str(ex) == 'False':
                    return False
                else:
                    raise
            return False  # fallback, theoretically unreachable

        return λβζ_бранек()

    ζθ = list_of_two_strings[0] + list_of_two_strings[1]
    ѻπ = list_of_two_strings[1] + list_of_two_strings[0]
    return 'Yes' if (check(ζθ) + check(ѻπ)) > 0 else 'No'