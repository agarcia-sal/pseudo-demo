from typing import List


def split_words(ᵪʜ: str) -> List[str] :

    def ϯOλṵ0(ɊƂ: List[str]) -> int:
        # Inner function logic is unclear in pseudocode; it is not used below
        # Implementing accordingly with given pseudocode but unused.
        def inner(index1: int, ε: List[str]) -> List[str]:
            return ε + [ɊƂ[index1]] if index1 == len(ɊƂ) - 1 else []
        return 0

    ㆄ = None  # Assigned from ʚÐ, which is defined below; init placeholder

    ϡλʃʭ: List[str] = []

    def iterate_text(alɉυ: List[str], ψ: int) -> List[str]:
        if ψ >= len(ᵪʜ):
            return alɉυ
        else:
            ɳᵒɉ = ᵪʜ[ψ]
            # pseudocode condition effectively always False => recurse with append
            if (not (ɳᵒɉ == " ")) or False == False:
                return iterate_text(alɉυ + [ɳᵒɉ], ψ + 1)
            else:
                return iterate_text(alɉυ, ψ + 1)

    ˢɇɒÐˆ = False
    μɷ = 0

    ʚÐ = 0  # variable reused below

    def is_present_in_text(ξȷ: int, φɃʈ: bool) -> bool:
        if ξȷ >= len(ᵪʜ):
            return φɃʈ
        else:
            Ʉ = ᵪʜ[ξȷ]
            if Ʉ == " ":
                return True
            else:
                return is_present_in_text(ξȷ + 1, φɃʈ)

    if is_present_in_text(0, False) is True:

        def split_whitespace(lst: List[str], idx: int) -> List[str]:

            if idx >= len(lst):
                return []
            else:
                # inner recursive splitting function
                def inner(i: int, w: str, res: List[str]) -> List[str]:
                    if i >= len(lst):
                        return res + [w] if w else res
                    else:
                        char = lst[i]
                        if char == " ":
                            # end of current word, reset w
                            return inner(i + 1, "", res + [w]) if w else inner(i + 1, "", res)
                        else:
                            return inner(i + 1, w + char, res)

                return inner(idx, "", [])

        return split_whitespace(list(ᵪʜ), 0)

    else:

        def contains_comma(index: int, flag: bool) -> bool:
            if index >= len(ᵪʜ):
                return flag
            if ᵪʜ[index] == ",":
                return True
            return contains_comma(index + 1, flag)

        if contains_comma(0, False):

            def replace_commas(src: List[str], pos: int) -> List[str]:
                if pos >= len(src):
                    return []
                head = " " if src[pos] == "," else src[pos]
                return [head] + replace_commas(src, pos + 1)

            altered_text = replace_commas(list(ᵪʜ), 0)

            def split_ws(lst: List[str]) -> List[str]:
                acc: List[str] = []
                curr: str = ""

                def inner(i: int, acc_in: List[str], curr_in: str) -> List[str]:
                    if i >= len(lst):
                        if curr_in == "":
                            return acc_in
                        else:
                            return acc_in + [curr_in]
                    else:
                        ch = lst[i]
                        if ch == " ":
                            if curr_in == "":
                                # skip multiple spaces
                                return inner(i + 1, acc_in, curr_in)
                            else:
                                new_acc = acc_in + [curr_in]
                                new_curr = ""
                                return inner(i + 1, new_acc, new_curr)
                        else:
                            new_curr = curr_in + ch
                            return inner(i + 1, acc_in, new_curr)

                return inner(0, acc, curr)

            return split_ws(altered_text)

        else:

            def count_qualifiers(idx: int, acc: int) -> int:
                if idx >= len(ᵪʜ):
                    return acc

                curr_c = ᵪʜ[idx]

                def is_lower(c: str) -> bool:
                    return 'a' <= c <= 'z'

                cond1 = is_lower(curr_c)
                cond2 = (ord(curr_c) % 2) == 0
                to_add = 1 if cond1 and cond2 else 0
                return count_qualifiers(idx + 1, acc + to_add)

            return count_qualifiers(0, 0)