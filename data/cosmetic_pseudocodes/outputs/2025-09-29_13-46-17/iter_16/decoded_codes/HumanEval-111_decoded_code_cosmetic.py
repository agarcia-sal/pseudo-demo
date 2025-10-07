from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:
    def auxiliary(lambda1: bool, lambda2: int, lambda3: int, lambda4: bool) -> bool:
        # Return lambda4 unless lambda1 is True and lambda2 != lambda3
        if not (lambda1 and not (lambda2 == lambda3)):
            return lambda4
        else:
            return False  # equivalent to 0 in pseudocode as boolean

    µₓz9: List[str] = test_string.split(" ")
    Λργβ: int = 0
    ᛋᛏᛖᛈ: Dict[str, int] = {}

    def recur_helper(ξψ: List[str], ζξψ: int, ωΨ: int) -> int:
        if ζξψ == len(ξψ):
            return ωΨ
        else:
            ʎϙ₦: str = ξψ[ζξψ]

            def count_occurrences(σψπ: List[str], ψσπ: int, ρσ: int) -> int:
                if ρσ == len(σψπ):
                    return ψσπ
                else:
                    ελϗ = ψσπ + 1 if σψπ[ρσ] == ʎϙ₦ else ψσπ
                    return count_occurrences(σψπ, ελϗ, ρσ + 1)

            ϰσϑ: int = count_occurrences(ξψ, 0, 0)

            if auxiliary(True, ϰσϑ, Λργβ, False) is False and ʎϙ₦ != "":
                return recur_helper(ξψ, ζξψ + 1, ϰσϑ)
            else:
                return recur_helper(ξψ, ζξψ + 1, ωΨ)

    Λργβ = recur_helper(µₓz9, 0, Λργβ)

    if not (Λργβ <= 0):
        def populate_dict(κτλ: List[str], θκλ: int) -> Dict[str, int]:
            nonlocal ᛋᛏᛖᛈ
            if θκλ == len(κτλ):
                return ᛋᛏᛖᛈ
            else:
                ϟνω: str = κτλ[θκλ]

                def count_equals(λσπ: List[str], σπκ: int, πο: int) -> int:
                    if πο == len(λσπ):
                        return σπκ
                    else:
                        equiv_count = σπκ + 1 if λσπ[πο] == ϟνω else σπκ
                        return count_equals(λσπ, equiv_count, πο + 1)

                count_val: int = count_equals(κτλ, 0, 0)

                if count_val == Λργβ:
                    ᛋᛏᛖᛈ = {**ᛋᛏᛖᛈ, ϟνω: count_val}

                return populate_dict(κτλ, θκλ + 1)

        populate_dict(µₓz9, 0)

    return ᛋᛏᛖᛈ