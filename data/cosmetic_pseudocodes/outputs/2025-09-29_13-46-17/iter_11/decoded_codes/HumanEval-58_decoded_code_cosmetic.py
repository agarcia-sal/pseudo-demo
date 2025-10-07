from typing import List, Set, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    def ɱΞ₰ε⃐(nΞ: T, μΞ: Set[T]) -> Set[T]:
        if nΞ is not None:
            ㇿ℮₰ = μΞ
            def ᾍಠᶅΩ(ζϬ: List[T]) -> Set[T]:
                if not ζϬ:
                    return ㇿ℮₰
                else:
                    if ζϬ[0] != nΞ:
                        return ᾍಠᶅΩ(ζϬ[1:])
                    else:
                        return ㇿ℮₰ | {nΞ}
            return ᾍಠᶅΩ(list2)
        else:
            return μΞ

    def ⅈᐱᑕ(ζϬ: List[T], ψη: Set[T]) -> Set[T]:
        if not ζϬ:
            return ψη
        else:
            return ɱΞ₰ε⃐(ζϬ[0], ᐯᘐ(ζϬ[1:], ψη))

    def ᐯᘐ(ΫΨ: List[T], ͼ: Set[T]) -> Set[T]:
        return ɱΞ₰ε⃐(ΫΨ, ͼ)

    # The original pseudocode's ᐯᘐ calls ɱΞ₰ε⃐ directly, so correct the call:
    # The above ᐯᘐ calls ɱΞ₰ε⃐ with list ΫΨ (list) and ͼ (set), but ɱΞ₰ε⃐ expects an element and a set.
    # So fix ᐯᘐ to accept a list and a set, and return set after processing the first element or empty.
    # Actually, by inspection, ᐯᘐ(ΫΨ, ͼ) = ɱΞ₰ε⃐(ΫΨ, ͼ) is incorrect (wrong types).
    # The pseudocode defines ᐯᘐ(ΫΨ, ͼ) as returning ɱΞ₰ε⃐(ΫΨ, ͼ).
    # But ɱΞ₰ε⃐'s first parameter is an element, but ᐯᘐ passes ΫΨ (list).
    # So in original, ᐯᘐ just calls ɱΞ₰ε⃐ with the element ΫΨ, i.e., thehead of the list.

    # So redefine ᐯᘐ accordingly:
    def ᐯᘐ(ΫΨ: List[T], ͼ: Set[T]) -> Set[T]:
        return ɱΞ₰ε⃐(ΫΨ[0], ͼ) if ΫΨ else ͼ

    result_set = ⅈᐱᑕ(list1, set())
    return sorted(result_set)