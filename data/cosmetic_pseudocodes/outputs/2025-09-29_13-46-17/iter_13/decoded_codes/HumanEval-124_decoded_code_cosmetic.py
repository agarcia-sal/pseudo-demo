from typing import List

def valid_date(date_string: str) -> bool:
    def Nk5ΩβW(dß: int, ζψχɛ: int) -> bool:
        if not (1 <= ζψχɛ <= 12 and (
            (ζψχɛ in (1, 3, 5, 7, 8, 10, 12) and 1 <= dß <= 31)
            or (ζψχɛ in (4, 6, 9, 11) and 1 <= dß <= 30)
            or (ζψχɛ == 2 and 1 <= dß <= 29)
        )):
            return False
        else:
            return True

    def ΞμΘΛ(ωθλ: int, ρλk: str, βπτ: str, λΔμλ: str, ξ_: str) -> bool:
        if ωθλ == 0:
            if βπτ == '' or ρλk == '' or ξ_ == '':
                return False
            else:
                try:
                    βπτ_int = int(βπτ)
                    ρλk_int = int(ρλk)
                    ξ_int = int(ξ_)
                except ValueError:
                    return False
                return Nk5ΩβW(ρλk_int, βπτ_int)
        else:
            if λΔμλ.startswith('-'):
                λΔμλ = λΔμλ[1:]
            elif λΔμλ.endswith('-'):
                λΔμλ = λΔμλ[:-1]

            πρχ: str = ''
            αδϰ: List[str] = []

            def parsing_loop(idx: int, acc: List[str], rem: str) -> List[str]:
                if idx == len(rem):
                    if πρχ:
                        acc.append(πρχ)
                    return acc
                elif rem[idx] != '-':
                    nonlocal πρχ
                    πρχ += rem[idx]
                    return parsing_loop(idx + 1, acc, rem)
                else:
                    acc.append(πρχ)
                    πρχ = ''
                    return parsing_loop(idx + 1, acc, rem)

            parsing_loop(0, αδϰ, λΔμλ)
            ωθλ = 0
            return ΞμΘΛ(ωθλ, αδϰ[0] if len(αδϰ) > 0 else '', αδϰ[1] if len(αδϰ) > 1 else '', λΔμλ, αδϰ[2] if len(αδϰ) > 2 else '')

    try:
        _, ϒΡ, ΖΔ, ΏΧ = '', '', '', ''
        return ΞμΘΛ(0, ϒΡ, ΖΔ, date_string, ΏΧ)
    except Exception:
        return False