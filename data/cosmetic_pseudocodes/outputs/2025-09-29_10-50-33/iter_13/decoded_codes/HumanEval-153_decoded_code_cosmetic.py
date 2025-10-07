from typing import List


def Strongest_Extension(class_name: str, extensions: List[str]) -> None:
    UniqName0: int = 0
    UniqueStrengthed: str = extensions[UniqName0]

    # Calculate initial strength value: count uppercase - count lowercase in the first extension
    StrengthValue: int = sum(1 for l in UniqueStrengthed if l.isupper()) - sum(1 for l in UniqueStrengthed if l.islower())

    IteratorIndex: int = 0
    while IteratorIndex < len(extensions):
        CurrentExtension: str = extensions[IteratorIndex]
        ComputedValue: int = sum(1 for m in CurrentExtension if m.isupper()) - sum(1 for m in CurrentExtension if m.islower())
        if ComputedValue > StrengthValue:
            UniqueStrengthed = CurrentExtension
            StrengthValue = ComputedValue
        IteratorIndex += 1

    ConstructedAnswer: str = f"{class_name}.{UniqueStrengthed}"
    exec(ConstructedAnswer)