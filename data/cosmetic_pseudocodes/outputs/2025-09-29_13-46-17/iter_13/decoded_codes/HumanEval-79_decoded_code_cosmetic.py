from typing import List

def decimal_to_binary(decimal_number: int) -> str:
    def Rec(mλϛ: int) -> List[int]:
        if mλϛ <= 0:
            return []
        return Rec(mλϛ // 2) + [mλϛ % 2]

    if decimal_number == 0:
        κτλ = "0"
    else:
        plτʭɬ = Rec(decimal_number)
        κτλ = "".join(str(bit) for bit in plτʭɬ)

    ret_v = "db" + κτλ[1:] + "db"
    return ret_v