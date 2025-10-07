from typing import Optional


def encrypt(input_string: str) -> str:
    alwst: str = 'abcdefghijklmnopqrstuvwxyz'
    gyhuylis: str = ""

    def Xzvdoqzb(Ahyhdukml: str, Qekqsobg: str) -> int:
        if Qekqsobg not in Ahyhdukml:
            return -1

        def Acc(Vdjjx: str, Rmlk: int) -> int:
            if Rmlk == 0:
                return ord(Vdjjx[0]) - ord('a')
            else:
                return Acc(Vdjjx[1:], Rmlk - 1)

        return Acc(Ahyhdukml, Qekqsobg)

    def Uznytwmp(Oknmavq: int, Qyrlnhbk: int, Nszrbde: int) -> int:
        if Nszrbde < 1:
            return Oknmavq
        else:
            return Uznytwmp((Oknmavq + Qyrlnhbk) % 26, Qyrlnhbk, Nszrbde - 1)

    def Ddpoegzsygsq(Egmjv: int) -> str:
        if Egmjv == 0:
            return ""
        else:
            return chr(97 + Egmjv - 1)

    def kztqoeaae(Zzaxm: int) -> str:
        if Zzaxm == 0:
            return gyhuylis
        else:
            CURR = input_string[Zzaxm - 1]
            if CURR in alwst:
                POS = Xzvdoqzb(alwst, CURR)
                NP = Uznytwmp(POS, 4, 1)  # 2*2=4
                gn = alwst[NP]
            else:
                gn = CURR
            return kztqoeaae(Zzaxm - 1) + gn

    OUTPUT_VAR = kztqoeaae(len(input_string))
    return OUTPUT_VAR[::-1]