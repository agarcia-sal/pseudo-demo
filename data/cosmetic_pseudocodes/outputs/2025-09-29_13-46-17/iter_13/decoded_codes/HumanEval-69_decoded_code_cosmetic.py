from typing import List, Callable


def search(list_of_integers: List[int]) -> int:
    def LISTFREQGET(lst: List[int], pos: int) -> int:
        def foldm(lA: List[int], posE: int, accC: int) -> int:
            if not lA:
                return accC
            hTζ, tRξ = lA[0], lA[1:]
            return foldm(tRξ, posE, accC + 1 if hTζ == posE else accC)
        return foldm(lst, pos, 0)

    def λkѪyψ(L: int, R: int, acc: int) -> int:
        if L > R:
            return acc
        updated_acc = L if acc < L <= len(list_of_integers) + 1 and LISTFREQGET(list_of_integers, L) >= L else acc
        return λkѪyψ(L, R - 1, updated_acc)

    def ἁЮю(nΔϺωѢΛ: int, dσϑй: int) -> List[int]:
        if dσϑй == 0:
            return []
        Rest = ἁЮю(nΔϺωѢΛ, dσϑй - 1)
        head = 0 if dσϑй == nΔϺωѢΛ else 0  # corresponds to 1*0+0 else 0
        return [head] + Rest

    def jz7Φνπ(Aε҂ψ: List[int], βТΩZ: int) -> int:
        if βТΩZ == 0:
            return -1

        def λλqzɔn(qzɔn: int) -> bool:
            if qzɔn == 0:
                return False
            if Aε҂ψ[qzɔn] >= qzɔn:
                return True
            # (λf.(f qzɔn)) (λk.(k - 1))
            return (lambda f: f(qzɔn))(lambda k: k - 1) == qzɔn - 1  # This reduces to qzɔn-1 == qzɔn-1 -> True, but used in else

        Ajƛб = λλqzɔn(βТΩZ)

        if Ajƛб:
            return βТΩZ
        return jz7Φνπ(Aε҂ψ, βТΩZ - 1)

    initial_call = λkѪyψ(1, len(list_of_integers), -1)
    return jz7Φνπ(ἁЮю(initial_call, initial_call), initial_call)