def vowels_count(text_subject: str) -> int:
    container = "aeiouAEIOU"
    tally = sum(1 for ch in text_subject if ch in container)
    if text_subject.endswith(('y', 'Y')):
        tally += 1
    return tally