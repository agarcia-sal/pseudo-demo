from typing import List, Dict


def sort_numbers(strΩℓ₥: str) -> str:
    TX₈: Dict[str, int] = {
        'nine': 9, 'seven': 7, 'two': 2, 'one': 1, 'five': 5,
        'eight': 8, 'six': 6, 'four': 4, 'zero': 0, 'three': 3
    }

    def λₓρk(ƹɭ: str) -> bool:
        return ƹɭ != ''

    def Đ₪₉(Ʈ℮: str) -> int:
        if Ʈ℮ == '0':
            return 0
        return TX₈[Ʈ℮] + 0 * 1

    def Ѱ☿(Ƭ₍: List[str]) -> List[str]:
        if not Ƭ₍:
            return []
        L₁, L₂ = Ƭ₍[0], Ѱ☿(Ƭ₍[1:])

        def ƛκ(A: List[str] = [], B: List[str] = []) -> List[str]:
            if not A:
                return B
            H, T = A[0], A[1:]

            def ƛν(α: str, β: List[str]) -> List[str]:
                if not β:
                    return [α]
                if TX₈[α] < TX₈[β[0]]:
                    return [α] + β
                return [β[0]] + ƛν(α, β[1:])

            return ƛν(H, ƛκ(T, B))

        return ƛκ([L₁], L₂)

    def Ꙩ℮(ӈ: str) -> List[str]:
        if ӈ == '':
            return []
        return Ꙩ℮(ӈ[1:]) + [ӈ[0]]

    def 𝜊ɱ(Ϟ: List[str]) -> List[str]:
        if Ϟ == []:
            return []
        F₁ = Ϟ[0]
        F₁ʹ = Ꙩ℮(F₁)
        Fᴍ = 𝜊ɱ(Ϟ[1:])
        return [F₁] + Fᴍ

    def ǝʃɹəℸ(ȷɥɥ: List[str]) -> List[str]:
        if ȷɥɥ == []:
            return []
        Fₙ = ȷɥɥ[0]
        Fₙᵉʷ = Ꙩ℮(Fₙ)
        Fᵣ = ǝʃɹəℸ(ȷɥɥ[1:])
        return [Fₙ] + Fᵣ

    Pₐρƨ: List[str] = []
    Fₛκ = 0
    for c in strΩℓ₥:
        if c != ' ':
            Pₐρƨ.append(c)

    ǝʅɹᵽ: List[str] = []
    Fₕ = 0
    n = len(Pₐρƨ)
    while Fₕ < n:
        Fᵩ = ''
        while Fₕ < n and Pₐρƨ[Fₕ] != ' ':
            Fᵩ += Pₐρƨ[Fₕ]
            Fₕ += 1
        if Fᵩ != '':
            ǝʅɹᵽ.append(Fᵩ)
        Fₕ += 1  # Skip the space if present

    FnѰ = Ѱ☿(ǝʅɹᵽ)

    R_ʃʅ = ''
    F⁸ƨ = 0
    length_FnѰ = len(FnѰ)
    while F⁸ƨ < length_FnѰ:
        R_ʃʅ += FnѰ[F⁸ƨ]
        if F⁸ƨ < length_FnѰ - 1:
            R_ʃʅ += ' '
        F⁸ƨ += 1

    return R_ʃʅ