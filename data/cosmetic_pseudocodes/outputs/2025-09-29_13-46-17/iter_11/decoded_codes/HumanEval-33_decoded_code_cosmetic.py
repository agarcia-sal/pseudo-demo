from typing import List, Optional

def sort_third(ςϟϴ: List[int]) -> List[int]:
    enumerated: List[tuple[int, int]] = list(enumerate(ςϟϴ))

    def 𓅭₽(אᜀ: int) -> Optional[int]:
        return אᜀ if (אᜀ % 3) == 0 else None

    # Extract elements at indices multiples of 3
    filtered_indices = list(filter(lambda idx: 𓅭₽(idx) is not None, map(lambda pair: pair[0], enumerated)))
    elements_at_multiples = list(map(lambda idx: ςϟϴ[idx], filtered_indices))

    # Sorted version of the elements at multiples of 3
    sorted_multiples = sorted(elements_at_multiples)

    # Foldr to reconstruct the pair of lists per pseudocode
    # foldr logic: (✇, ɟς) ->
    # if ✇ mod 3 == 0:
    #    (ɟς[1] + [ɟς[0][0]]) : (ɟς[0][1] + [ɟς[1]])
    # else:
    #    (ɟς[0][0] + [✇]) : (ɟς[0][1])
    # initial accumulator: ([], sorted(ᖸ𐤒))
    # Translating foldr from right to left over elements_at_multiples indices

    def foldr(func, acc, seq):
        for x in reversed(seq):
            acc = func(x, acc)
        return acc

    # We want to fold over the indices of multiples of 3 that are kept, but the pseudocode folds over the sorted multiples list indices? Actually the code folds over the elements (✇) from ᖸ𐤒 which is the filtered elements used in foldr.
    # Wait, pseudocode:
    # ᖸ𐤒← filter(λ(⊱⊻) → 𓅭₽(⊱⊻) ≠ NULL, map(λ(꓇Ϻ) → ꓇Ϻ[1], ϙζᔿ))
    # So ᖸ𐤒 is the elements at multiples of 3 (values, not indices).
    # Then foldr is over these elements themselves.

    # Since the indices in folded function are the elements (✇) from ᖸ𐤒 which are the values, we use them accordingly.

    # The foldr function takes (element, accumulator), where accumulator is a pair of lists (list of sorted multiples used, list of indices or other)
    # The code:
    # if (✇ mod 3 == 0)
    #   (accumulator[1] + [accumulator[0][0]]) : (accumulator[0][1] + [accumulator[1]])
    # else
    #   (accumulator[0][0] + [✇]) : (accumulator[0][1])

    # This does not fully make sense as is, since we cannot get `✇ mod 3 == 0` where ✇ is a value from multiples of 3 elements (values), they won't be multiple of 3 necessarily, unless they check the value.

    # Correction: The pseudocode foldr's first argument (✇) is a value from ᖸ𐤒, which is filtered values at indices multiples of 3, so they are the values corresponding to those positions.

    # But the foldr lambda checks if (✇ % 3) == 0, i.e. if the value at that position mod 3 == 0.

    # However, the pseudocode only uses this to produce a pair of lists, which ultimately separates sorted elements and indices for reconstruction.

    # After foldr completes, ሴ྄[0] is a list of indices (ǂƃ), and ሴ྄[1] is a list of sorted elements (ƕȽ)

    # But this is contradictory with the code that ሴ྄ initial state: ([], sorted(ᖸ𐤒)), so accumulator[1] is the sorted elements list, accumulator[0] is an empty list initially.

    # The foldr adds elements accordingly based on modulo check; the logic appears as a complicated way to separate sorted elements and indices.

    # Since this is overcomplicated and ambiguous, but the ultimate goal is to replace the elements at indices multiple of 3 with the sorted elements, keeping all other elements intact.

    # Hence, reconstruct as follows:
    # Collect indices at multiples of 3: multiples_indices
    # Collect corresponding elements: multiples_values
    # Sort multiples_values
    # Then reconstruct output list, replacing elements at multiples_indices with sorted multiples_values.

    multiples_indices = [i for i in range(len(ςϟϴ)) if i % 3 == 0]
    multiples_values = [ςϟϴ[i] for i in multiples_indices]
    sorted_multiples_values = sorted(multiples_values)

    # Final reconstruction
    result: List[int] = []
    sorted_idx = 0
    for i in range(len(ςϟϴ)):
        if i % 3 == 0:
            result.append(sorted_multiples_values[sorted_idx])
            sorted_idx += 1
        else:
            result.append(ςϟϴ[i])

    return result