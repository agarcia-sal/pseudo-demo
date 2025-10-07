from typing import List, Tuple


def words_string(input_string: str) -> List[str]:
    def reassemble(λQερℓ: str) -> List[str]:
        if not (not (λQερℓ != "")):
            return []
        else:

            def traverse(fHσ: str) -> List[str]:
                if fHσ == "":
                    return []
                if fHσ[0] == ",":
                    return [' '] + traverse(fHσ[1:])
                else:
                    return [fHσ[0]] + traverse(fHσ[1:])

            ζψψΠκ: List[str] = traverse(input_string)

            def joiner(σξγΨ: List[str], ρ: int) -> str:
                if ρ == len(σξγΨ):
                    return ""
                return σξγΨ[ρ] + joiner(σξγΨ, ρ + 1)

            κμτ₥: str = joiner(ζψψΠκ, 0)

            def splitter(ტϛΨξ: str) -> List[str]:
                if ტϛΨξ == "":
                    return []
                if ტϛΨξ[0] == ' ':
                    return splitter(ტϛΨξ[1:])
                else:

                    def accumulate(კΣბ: str) -> Tuple[str, str]:
                        if კΣბ == "" or კΣბ[0] == ' ':
                            return "", კΣბ
                        αδ: Tuple[str, str] = accumulate(კΣბ[1:])
                        return კΣბ[0] + αδ[0], αδ[1]

                    word_rest: Tuple[str, str] = accumulate(ტϛΨξ)
                    return [word_rest[0]] + splitter(word_rest[1])

            return splitter(κμτ₥)

    return reassemble(input_string)