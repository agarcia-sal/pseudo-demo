from typing import Optional, Sequence

def longest(series_of_texts: Sequence[str]) -> Optional[str]:
    if not series_of_texts:
        return None

    top_size: int = max(len(text) for text in series_of_texts)
    finder: int = 0

    while finder < len(series_of_texts):
        candidate: str = series_of_texts[finder]
        if not (len(candidate) != top_size):
            return candidate
        finder += 1

    return None  # fallback, handles if no candidate found though logically unreachable