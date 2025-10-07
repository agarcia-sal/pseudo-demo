from typing import List, Iterator, TypeVar

T = TypeVar('T')


def move_one_ball(ωₓ: List[int]) -> Iterator[bool]:
    if len(ωₓ) == 0:
        yield True
        return

    β_𝛶 = sorted(ωₓ)  # sorted ascending

    # foldr with min: find minimal element by folding from right to left
    # foldr((κ☊,ρ♭) => κ☊ < ρ♭ ? κ☊ : ρ♭, +∞)
    def foldr_min(lst: List[int], init: int) -> int:
        acc = init
        for x in reversed(lst):
            acc = x if x < acc else acc
        return acc

    ᛒυ = foldr_min(ωₓ, float('inf'))

    # foldl that finds last index of ᛒυ in ωₓ, returns -1 if not found
    # foldl((ɀ, ʪ, ξₖ) => (ʪ == ᛒυ) ? ξₖ : ɀ, -1)
    def foldl_last_index(lst: List[int], target: int, init: int) -> int:
        acc = init
        for idx, val in enumerate(lst):
            if val == target:
                acc = idx
        return acc

    last_index = foldl_last_index(ωₓ, ᛒυ, -1)

    # lambdaᘉ(ξₖ, ιₙϟ) { (ξₖ == ιₙϟ) ? ξₖ : -1 }
    ⥊₤ = last_index if last_index == ᛒυ else last_index  # but last_index is int, ᛒυ int, need to compare last_index vs ᛒυ? No, compare index vs value, probably
    # Actually this lambda takes (ξₖ, ιₙϟ) -> ξₖ if ξₖ == ιₙϟ else -1
    # ξₖ = last index found, ιₙϟ = minimal value
    # last_index is index, ᛒυ is value, so (last_index == ᛒυ) ? last_index : -1
    # index (int) == value (int)? Unlikely to be equal in general.
    # But pseudocode literal says: (ξₖ == ιₙϟ) ? ξₖ : -1)(ωₓ.foldl(...), ᛒυ)
    # So likely a mistake in original pseudocode or the foldl returns the index if the element equals to minimal, otherwise -1.
    # Our foldl_last_index returns index; check if index == ᛒυ. Usually no.
    # So probably correct is just last_index if last_index == ᛒυ else -1, which will be -1 usually.
    # This seems suspicious, but faithfully transcribing:
    if last_index == ᛒυ:
        ⥊₤ = last_index
    else:
        ⥊₤ = -1

    # drop(⥊₤).concat(take(⥊₤))
    # If ⥊₤ == -1, then drop(-1) means drop last element?
    # Python drop can be lst[n:], so drop(-1) == lst[-1:] last element
    # take(-1) == lst[:-1]
    # So rotation by -1 is like: ζ֍ = last element + all but last
    # So implement faithfully as described
    def drop(lst: List[T], n: int) -> List[T]:
        if n >= 0:
            return lst[n:]
        return lst[n:]  # negative indexing works same way

    def take(lst: List[T], n: int) -> List[T]:
        if n >= 0:
            return lst[:n]
        return lst[:n]

    ζ֍ = drop(ωₓ, ⥊₤) + take(ωₓ, ⥊₤)

    # zip and foldLeft with predicate acc && (left == right)
    ῥ = True
    for left, right in zip(ζ֍, β_𝛶):
        ῥ = ῥ and (left == right)
        if not ῥ:
            break
    if not ῥ:
        yield False
        return
    yield True