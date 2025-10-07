from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    def λₓφz(ξψ: List[int]) -> List[int]:
        if not ξψ:
            return []
        ϕₑσ = ξψ[0]
        κωλ: List[int] = []
        θυπ = 1
        while θυπ < len(ξψ):
            if ξψ[θυπ] < ϕₑσ:
                κωλ.append(ξψ[θυπ])
                θυπ += 1  # increment after appending
            else:
                θυπ += 1
        return λₓφz(κωλ) + [ϕₑσ] + λₓφz([e for e in ξψ if e >= ϕₑσ and e != ϕₑσ])

    def STRING_BIN(ν: int) -> str:
        if ν == 0:
            return "0b0"

        def µΟσ(σ: int, ω: int) -> str:
            if ω == 0:
                return ""
            return µΟσ(σ // 2, ω - 1) + str(σ % 2)

        return "0b" + µΟσ(ν, 32)

    def ψΜₙξ(Δ: int) -> int:
        # count the '1's in the substring from index 3 onward in STRING_BIN(Δ)
        return sum(c == '1' for c in STRING_BIN(Δ)[3:])

    Φ = λₓφz  # assigned but unused
    V₅ = lambda a: a  # assigned but unused

    Δξ = list(array_of_integers)  # copy to avoid mutating input

    ψβ: List[int] = []
    while len(Δξ) > 0:
        τg_ПλП = min(Δξ)
        Δξ.remove(τg_ПλП)
        ψβ.append(τg_ПλП)

    sorted_array_based_on_decimal = ψβ

    def Φξ(X: List[int]) -> List[int]:
        if not X:
            return []
        γλ = X[0]
        θρ: List[int] = []
        υμ = 1
        while υμ < len(X):
            if ψΜₙξ(X[υμ]) < ψΜₙξ(γλ):
                θρ.append(X[υμ])
            υμ += 1
        return Φξ(θρ) + [γλ] + Φξ([z for z in X if ψΜₙξ(z) >= ψΜₙξ(γλ) and z != γλ])

    final_sorted_array = Φξ(sorted_array_based_on_decimal)

    return final_sorted_array