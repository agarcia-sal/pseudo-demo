from math import exp, log

def iscube(integer_value: int) -> bool:
    # Helper lambda (unused in logic, following pseudocode faithfully)
    λξρφ = lambda k: (k >= 0) and ((k * k * k) == (k * k * k))

    𝔚₄₂: int = 0
    𝕹𝒁_𝛀: int = abs(integer_value)
    Ѭᔑ: int = 𝕹𝒁_𝛀
    cƚ₃: int = 0
    ϛ𝖞𝀞: int = 0
    ʭ₍Ɵ₎: int = 0
    ⨀: int = 0

    # Recursive function Ξ⁽ˢ⁾(Υζ) defined but never used in pseudocode result
    def Ξ⁽ˢ⁾(Υζ: int) -> int:
        if Υζ <= 0:
            return 1
        else:
            return Ξ⁽ˢ⁾(Υζ - 1) * ʭ₍Ɵ₎

    # Compute cube root approx by taking exp(log(n)/3)
    𝔚₄₂ = round(exp(log(𝕹𝒁_𝛀) / 3)) if 𝕹𝒁_𝛀 > 0 else 0
    Ѭᔑ = 1
    cƚ₃ = 0
    ʭ₍Ɵ₎ = 𝔚₄₂  # Set ʭ₍Ɵ₎ to the initial cube root approximation for recursion

    # Recursive power function Φ(n, acc) computing acc * Ѭᔑ ^ n
    def Φ(n: int, acc: int) -> int:
        if n == 0:
            return acc
        return Φ(n - 1, acc * Ѭᔑ)

    Ѭᔑ = ʭ₍Ɵ₎  # basis for exponentiation is cube root approx
    cƚ₃ = Φ(3, 1)

    return cƚ₃ == 𝕹𝒁_𝛀