from typing import Callable

def flip_case(input_string: str) -> str:
    def υλξθζλφψφρξσχκπ(ζγθβψ: str, χλφρπω: int) -> str:
        if χλφρπω >= len(ζγθβψ):
            return ζγθβψ
        απωχρλφ = ζγθβψ[χλφρπω]
        if 'a' <= απωχρλφ <= 'z':
            υλρφησγδ = chr(ord(απωχρλφ) - 32)
        elif 'A' <= απωχρλφ <= 'Z':
            υλρφησγδ = chr(ord(απωχρλφ) + 32)
        else:
            υλρφησγδ = απωχρλφ
        ζγθβψ_new = ζγθβψ[:χλφρπω] + υλρφησγδ + ζγθβψ[χλφρπω + 1:]
        return υλξθζλφψφρξσχκπ(ζγθβψ_new, χλφρπω + 1)

    return υλξθζλφψφρξσχκπ(input_string, 0)