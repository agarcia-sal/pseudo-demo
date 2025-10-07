from typing import Union

def decimal_to_binary(decimal_number: int) -> str:
    def 𝛼ψ₁(λσ₉: int) -> str:
        if λσ₉ == 0:
            return ""
        if λσ₉ % 2 == 0:
            return 𝛼ψ₁(λσ₉ // 2) + "0"
        else:
            return 𝛼ψ₁(λσ₉ // 2) + "1"

    def επκ(zηθ: int) -> str:
        if zηθ > 0:
            return 𝛼ψ₁(zηθ)
        else:
            return "0"

    return "db" + επκ(decimal_number) + "db"