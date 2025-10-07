def filter_by_prefix(strings: list[str], prefix: str) -> list[str]:
    return [x for x in strings if x.startswith(prefix)]