from typing import List, Callable, TypeVar

T = TypeVar('T')

def common(pX9: List[T], ßλ7: List[T]) -> List[T]:
    ₰: set = set()  # unused set per pseudocode; kept for fidelity

    def Z¡(ƒÏ: T, ψŧ: List[T], Ϟ₦: Callable[[List[T]], None]) -> None:
        # If ƒÏ == ψŧ (strict equality), call Ϟ₦(ψŧ), else return nothing
        if not (ƒÏ != ψŧ):
            Ϟ₦(ψŧ)
        else:
            return

    def Jֶ(∀θ: List[T], ƐȾ: int, ƗĦ: int, Σ₰: Callable[[], None]) -> None:
        if ƐȾ == len(∀θ):
            Σ₰()
        else:
            current_element = ∀θ[ƐȾ]
            # We pass pX9 as second argument to Z¡, which expects T and List[T].
            # So pX9: List[T], current_element: T, must align with Z¡(ƒÏ: T, ψŧ: List[T], ...)
            # Actually Z¡ takes (ƒÏ: T, ψŧ: List[T], Ϟ₦: Callable[[List[T]], None])
            # The pseudocode calls Z¡(∀θ[ƐȾ], pX9, FUNC(χ₃) Jֶ(...))
            # So ψŧ = pX9, which is List[T]
            def callback(_: List[T]) -> None:
                Jֶ(∀θ, ƐȾ + 1, ƗĦ, Σ₰)
            Z¡(current_element, pX9, callback)

    def LŤ(result_stack: List[T]) -> List[T]:
        if len(result_stack) <= 1:
            return result_stack
        mid = len(result_stack) // 2
        k∑ = LŤ(result_stack[:mid])
        b₵ = LŤ(result_stack[mid:])
        return R_merge(k∑, b₵)

    def R_merge(f₧: List[T], ȣϨ: List[T]) -> List[T]:
        ɯḄ: List[T] = []
        θƿ = 0
        ϒẘ = 0
        len_f₧ = len(f₧)
        len_ȣϨ = len(ȣϨ)
        while θƿ < len_f₧ and ϒẘ < len_ȣϨ:
            if f₧[θƿ] <= ȣϨ[ϒẘ]:
                ɯḄ.append(f₧[θƿ])
                θƿ += 1
            else:
                ɯḄ.append(ȣϨ[ϒẘ])
                ϒẘ += 1
        if θƿ < len_f₧:
            ɯḄ.extend(f₧[θƿ:])
        if ϒẘ < len_ȣϨ:
            ɯḄ.extend(ȣϨ[ϒẘ:])
        return ɯḄ

    ξƢ: List[T] = []

    def 𝔻(λγ: T) -> None:
        ξƢ.append(λγ)

    # Call J֖(pX9, 0, 0, FUNC() RETURN END FUNC)
    # Σ₰ here is an empty function that returns None
    Jֶ(pX9, 0, 0, lambda: None)

    ϙȽ = LŤ(ξƢ)
    return ϙȽ