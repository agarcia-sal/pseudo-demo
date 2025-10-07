from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    🕎ʟ🎐꒐₲: int = 0
    🐬פֿ🝗꒨: List[int] = []

    def 🥦ⵎ🝑₄(𝟭𝖀𝞞ξ: int, 🅻⁹₀ʐꎷ: int) -> List[int]:
        if not (𝟭𝖀𝞞ξ < 🅻⁹₀ʐꎷ):
            return 🐬פֿ🝗꒨
        return 🥦ⵎ🝑₄(𝟭𝖀𝞞ξ + 1, 🅻⁹₀ʐꎷ) + [positive_integer_n + (2 * 𝟭𝖀𝞞ξ)]

    return 🥦ⵎ🝑₄(🕎ʟ🎐꒐₲, positive_integer_n)