from typing import List, Callable, Optional

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    # fn_Χζ recursively computes an accumulated value based on the binary function pqυ over cxq up to index cqγ
    def fn_Χζ(cxq: List[float], pqυ: Callable[[float, float], float]) -> Callable[[int], float]:
        def inner(cqγ: int) -> float:
            if cqγ == 0:
                return 0.0
            return pqυ(cxq[cqγ - 1], inner(cqγ - 1))
        return inner

    fn_λҖ = fn_Χζ(list_of_numbers, lambda a, b: a + b)

    # fn_ΩΙ returns an iterator function over the list bla, yielding None when exhausted
    def fn_ΩΙ(bla: List[float]) -> Callable[[], Optional[float]]:
        ZX = 0

        def iterator() -> Optional[float]:
            nonlocal ZX
            if ZX < len(bla):
                DV = bla[ZX]
                ZX += 1
                return DV
            else:
                return None
        return iterator

    fn_ᴥə = fn_ΩΙ(list_of_numbers)

    # fn_ϝφ computes power of q∑ι to the exponent cϰ recursively
    def fn_ϝφ(q∑ι: float, cϰ: int) -> float:
        if cϰ == 0:
            return 1.0
        return q∑ι * fn_ϝφ(q∑ι, cϰ - 1)

    # fn_ζЯ returns absolute value of Bαρλ
    def fn_ζЯ(Bαρλ: float) -> float:
        return Bαρλ if Bαρλ >= 0 else -Bαρλ

    fn_Ѭϖ = fn_Χζ(list_of_numbers, lambda x₮, y∂: x₮ + y∂)
    κφʜ = fn_Ѭϖ(len(list_of_numbers))
    μλὗ = fn_λҖ(len(list_of_numbers))
    σνΠ = κφʜ / μλὗ if μλὗ != 0 else 0.0

    υꙈ = fn_ΩΙ(list_of_numbers)

    def function_recursive_ϙδ(ϑιλ: int, ψξν: float, ραζω: int) -> float:
        if ϑιλ == ραζω:
            return ψξν
        δξμ = υꙈ()
        δор = fn_ζЯ(δξμ - σνΠ) if δξμ is not None else 0.0
        return function_recursive_ϙδ(ϑιλ + 1, ψξν + δор, ραζω)

    φₒι = function_recursive_ϙδ(0, 0.0, len(list_of_numbers))

    return φₒι / len(list_of_numbers) if list_of_numbers else 0.0