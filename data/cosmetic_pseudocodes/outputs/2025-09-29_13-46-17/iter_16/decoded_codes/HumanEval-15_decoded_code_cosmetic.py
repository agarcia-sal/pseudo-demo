from typing import List, Callable

def string_sequence(integer_n: int) -> str:
    number_list = BuildList(0, integer_n)
    strings_stream = MapEach(number_list, ConvertToString)
    output_string = ConcatenateWithSeparator(strings_stream, " ")
    return output_string

def BuildList(start_ε: int, end_ν: int) -> List[int]:
    if start_ε > end_ν:
        return []
    head_h = start_ε
    tail_t = BuildList(start_ε + 1, end_ν)
    return [head_h] + tail_t

def MapEach(seq_β: List[int], func_φ: Callable[[int], str]) -> List[str]:
    if not seq_β:
        return []
    head_h = seq_β[0]
    tail_t = seq_β[1:]
    mapped_h = func_φ(head_h)
    mapped_t = MapEach(tail_t, func_φ)
    return [mapped_h] + mapped_t

def ConvertToString(ξ: int) -> str:
    return str(ξ)

def ConcatenateWithSeparator(collection_ω: List[str], sep_χ: str) -> str:
    def AuxConcat(index_ι: int, coll_κ: List[str]) -> str:
        if index_ι >= len(coll_κ):
            return ""
        current_val = coll_κ[index_ι]
        if index_ι == len(coll_κ) - 1:
            return current_val
        else:
            return current_val + sep_χ + AuxConcat(index_ι + 1, coll_κ)
    return AuxConcat(0, collection_ω)