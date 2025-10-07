from typing import List

def sort_numbers(exchange_list: str) -> str:
    conversion_table: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    tokens: List[str] = [piece for piece in exchange_list.split(" ") if piece]

    tokens.sort(key=lambda x: conversion_table[x])  # Sort tokens by numeric value

    return " ".join(tokens)