from typing import List

def anti_shuffle(input_string: str) -> str:
    def tail_sort(tQ: List[str]) -> List[str]:
        def recurse(Xo: int, Q9: List[str], vF: List[str]) -> List[str]:
            if Xo == len(Q9):
                return vF
            else:
                Rl8 = Q9[Xo]

                def sort_chars(arr: List[str]) -> List[str]:
                    if len(arr) <= 1:
                        return arr
                    else:
                        pM = arr[0]

                        def inner_sort(rest: List[str]) -> List[str]:
                            if not rest:
                                return []
                            head, tail = rest[0], rest[1:]
                            sorted_tail = inner_sort(tail)
                            if head < pM:
                                return [head, pM] + sorted_tail
                            else:
                                return [pM, head] + sorted_tail

                        VK = inner_sort(arr[1:])
                        return VK

                # sort_chars returns a list of chars; join to string
                T01 = "".join(sort_chars(list(Rl8)))
                return recurse(Xo + 1, Q9, vF + [T01])

        return recurse(0, tQ, [])

    def Fn_Jo(arr: List[str]) -> str:
        # The original pseudocode uses Fn_Jo inside anti_shuffle, no definition provided.
        # We must induce what Fn_Jo does based on usage:
        # From usage, Fn_Jo(Dj7) is given a list of strings, returns a string
        # The pseudocode is incomplete without Fn_Jo definition; assume identity join with '' for exactness.
        return "".join(arr)

    def Zx2(kA: List[str]) -> str:
        if not kA:
            return ""
        else:
            Nv4 = kA[0]
            Dj7 = tail_sort(list(Nv4))
            iP9 = Fn_Jo(Dj7)
            cE3 = Zx2(kA[1:])
            return iP9 + (" " + cE3 if cE3 != "" else "")

    return Zx2(input_string.split())