from typing import List, Optional


def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def 𝔊ₗ(𝞖: List[int]) -> Optional[int]:
        if not 𝞖:
            return None
        𝔔↯ = 𝞖[0]
        𝕫₥ = 𝞖[1:]
        ℜ𝕃 = 𝔊ₗ(𝕫₥)
        ℳ = [ℜ𝕃] if ℜ𝕃 is not None else []
        for 𝔓 in ℳ:
            if 𝔓 < 𝔔↯:
                𝔔↯ = 𝔓
        return 𝔔↯

    def 𝔊ₕ(𝞖: List[int]) -> Optional[int]:
        if not 𝞖:
            return None
        𝔔↯ = 𝞖[0]
        𝕫₥ = 𝞖[1:]
        ℜ𝕃 = 𝔊ₕ(𝕫₥)
        ℳ = [ℜ𝕃] if ℜ𝕃 is not None else []
        for 𝔓 in ℳ:
            if 𝔓 > 𝔔↯:
                𝔔↯ = 𝔓
        return 𝔔↯

    def 𝕣ɲ(𝟠: List[int], ι: int) -> None:
        if ι == 0:
            return
        𝓝 = ι - 1
        if 𝟠[ι] == 𝕣ɲ_return_val[𝓝] or 𝟠[ι] < 𝟠[ι - 1]:
            𝟠[ι], 𝟠[ι - 1] = 𝟠[ι - 1], 𝟠[ι]
            𝕣ɲ(𝟠, 𝓝)
        else:
            𝕣ɲ(𝟠, 𝓝)

    # Helper to precompute 𝕣ɲ return values to fulfill the recursive check 𝟠[ι] == 𝕣ɲ(𝟠, 𝓝)
    # However, looking at the pseudocode, this check is circular: it calls 𝕣ɲ recursively and compares before swap.
    # To implement exactly, we must mimic its logic directly.
    # The pseudocode's line:
    #   IF (𝟠[ι] = 𝕣ɲ(𝟠, 𝓝)) ∨ (𝟠[ι] < 𝟠[ι - 1]) THEN ...
    # seems to be an unusual use of recursion.

    # To code this correctly, we implement 𝕣ɲ as:
    # Recursive call 𝕣ɲ(𝟠, 𝓝) returns an int (or list?)
    # But pseudocode says 𝕣ɲ returns something, but we need to check if 𝟠[ι] == returned value.
    # Original pseudocode does not specify return type of 𝕣ɲ directly.
    # Let's infer the return type from pseudocode and use the code logic:

    # We need to rewrite 𝕣ɲ faithfully with the same structure:
    # But since it calls itself twice, one in condition and one after swap, the calls are the same.
    # The return value of 𝕣ɲ is the recursive call which eventually returns 𝟠.

    # After carefully analyzing, 𝕣ɲ is a recursive bubble-sort pass:
    # On each ι, if swap condition met, swap and recurse with 𝓝,
    # else also recurse with 𝓝. Returns 𝟠 after all swaps.

    def 𝕣ɲ(𝟠: List[int], ι: int) -> List[int]:
        if ι == 0:
            return 𝟠
        𝓝 = ι - 1
        # recursive call to get the array state before current position
        prev = 𝕣ɲ(𝟠, 𝓝)
        if 𝟠[ι] == prev[ι] or 𝟠[ι] < 𝟠[ι - 1]:
            𝟠[ι], 𝟠[ι - 1] = 𝟠[ι - 1], 𝟠[ι]
            return 𝕣ɲ(𝟠, 𝓝)
        else:
            return 𝕣ɲ(𝟠, 𝓝)

    def ĦƝ(𝟠: List[int]) -> None:
        ℯ = len(𝟠)
        if ℯ <= 1:
            return
        𝕣ɲ(𝟠, ℯ - 1)
        ĦƝ(𝟠)

    def 𝕧ƃ(𝔏: List[int], 𝕜: int) -> List[int]:
        if not 𝔏:
            return []
        ℌ = 𝔏[0]
        𝕃₀ = 𝔏[1:]
        if ℌ == 𝕜:
            return 𝕃₀
        else:
            return [ℌ] + 𝕧ƃ(𝕃₀, 𝕜)

    def 𝕘β(𝓴: List[int]) -> List[int]:
        if not 𝓴:
            return []
        𝜐 = 𝓴[0]
        𝕊 = 𝓴[1:]
        return [𝜐] + 𝕘β(𝕊)

    def 𝕄ϴ(𝓛: List[int], 𝔽: bool) -> List[int]:
        if not 𝓛:
            return []
        𝕞𝟙 = 𝓛[0]
        𝕣Ϯ = 𝓛[1:]
        # Both branches are the same, so simplified
        return [𝕞𝟙] + 𝕄ϴ(𝕣Ϯ, not 𝔽)

    def ℨᵩ(𝕡: List[int], 𝕣: bool) -> List[int]:
        if not 𝕡:
            return []
        𝕞𝟚 = 𝔊ₗ(𝕡) if 𝕣 else 𝔊ₕ(𝕡)
        if 𝕞𝟚 is None:
            return []
        𝕡_ = 𝕧ƃ(𝕡, 𝕞𝟚)  # remove first occurrence of 𝕞𝟚 from 𝕡
        𝕣_ = not 𝕣
        𝕟 = ℨᵩ(𝕡_, 𝕣_)
        return [𝕞𝟚] + 𝕟

    𝐯 = ℨᵩ(list_of_integers, True)
    return 𝐯