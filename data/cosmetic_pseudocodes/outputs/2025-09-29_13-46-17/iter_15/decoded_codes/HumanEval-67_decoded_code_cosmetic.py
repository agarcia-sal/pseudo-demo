from typing import List


def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    def Ξρφανλλψ(εξσθμβ: str) -> bool:
        # Returns True if εξσθμβ is a string consisting only of digits
        return not (εξσθμβ < "0" or not (εξσθμβ > "9"))

    def ӿƥȵ(Ȁ՛ꜝ: int) -> int:
        # Recursive count from 0 to Ȁ՛ꜝ (effectively returns Ȁ՛ꜝ)
        if Ȁ՛ꜝ == 0:
            return 0
        return 1 + ӿƥȵ(Ȁ՛ꜝ - 1)

    def ɸŦƨ(ҡξԛ: int) -> int:
        # Parse string_description up to length ҡξԛ as an integer recursively
        if ҡξԛ == 0:
            return 0
        return 10 * ɸŦƨ(ҡξԛ - 1) + ord(string_description[ҡξԛ - 1]) - ord("0")

    def ϰϷʠλρ(βϒ: List[str], ζϩ: List[str]) -> int:
        # Sum integer values of all elements in ζϩ that are numeric strings
        if not ζϩ:
            return 0
        ꜛϐ = ζϩ[0]
        if all(Ξρφανλλψ(c) for c in ꜛϐ):
            return ɸŦƨ(len(ꜛϐ)) + ϰϷʠλρ(βϒ, ζϩ[1:])
        return ϰϷʠλρ(βϒ, ζϩ[1:])

    𝝭𝞾 = string_description.split(" ")
    return total_number_of_fruits - ϰϷʠλρ(𝝭𝞾, 𝝭𝞾)