from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    idxTemp: int = 0
    maxDiff: int = sum('A' <= x <= 'Z' for x in extensions[0]) - sum('a' <= x <= 'z' for x in extensions[0])
    while idxTemp < len(extensions):
        currentDiff = sum('A' <= c <= 'Z' for c in extensions[idxTemp]) - sum('a' <= c <= 'z' for c in extensions[idxTemp])
        if currentDiff > maxDiff:
            maxDiff = currentDiff
        idxTemp += 1
    return f"{class_name}.{extensions[idxTemp - 1]}"