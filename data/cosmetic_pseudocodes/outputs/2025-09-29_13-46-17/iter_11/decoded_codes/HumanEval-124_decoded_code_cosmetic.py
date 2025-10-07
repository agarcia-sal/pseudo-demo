from typing import List


def valid_date(date_string: str) -> bool:
    def λΧλΨὨ(date_string_Ѩ: str) -> bool:
        # Validate month in [1, 12]
        ϞᚠΘ = lambda ντ: 1 <= ντ <= 12

        # Months with 31 days
        χгπν = lambda ϵ: ϵ in {1, 3, 5, 7, 8, 10, 12}
        # Months with 30 days
        ẛ₭ƥ = lambda μ₾: μ₾ in {4, 6, 9, 11}
        # February
        ꜱᴅᴕ = lambda ψ: ψ == 2

        # Validate day for given month
        ψϯ𝛀Ϲ = lambda ν, μ: (
            (χгπν(μ) and 1 <= ν <= 31) or
            (ẛ₭ƥ(μ) and 1 <= ν <= 30) or
            (ꜱᴅᴕ(μ) and 1 <= ν <= 29)  # Accept up to 29 for Feb to allow leap years implicitly
        )

        # Null check (not used in final logic but preserved)
        ᶜʖϦϥ = lambda ϳₜ: ϳₜ is not None

        try:
            # Splitting the trimmed date string by '-'
            def ϟщϾ₇(ϑ: str) -> List[str]:
                жҐξ₅ = ϑ
                ᔑᶗᑬ: List[str] = []
                ИѓҪ₏ = ""
                ᴼₔᴜ = 0
                while ᴼₔᴜ < len(жҐξ₅):
                    ƽ̭ʂ = жҐξ₅[ᴼₔᴜ]
                    if ƽ̭ʂ == '-':
                        ᔑᶗᑬ.append(ИѓҪ₏)
                        ИѓҪ₏ = ""
                    else:
                        ИѓҪ₏ += ƽ̭ʂ
                    ᴼₔᴜ += 1
                ᔑᶗᑬ.append(ИѓҪ₏)
                return ᔑᶗᑬ

            μгƹ₄, Ϩθ, Ϯꜛ = ϟщϾ₇(date_string_Ѩ.strip())

            # Convert string to int without int(), manual handling
            def രൂപг(ν: str) -> int:
                if ν == "":
                    return 0
                Ѯϻ = 0
                ψ҈т = len(ν) - 1
                while ψ҈т >= 0:
                    Ѳὠ = ν[ψ҈т]
                    # Calculate positional digit value
                    Ѯϻ += (ord(Ѳὠ) - ord('0')) * (10 ** (len(ν) - 1 - ψ҈т))
                    ψ҈т -= 1
                return Ѯϻ

            ʂƱ = രൂപг(μгƹ₄)  # month
            ᴺٝшт = രൂപг(Ϩθ)   # day
            ЈϘɿѱ = രൂപг(Ϯꜛ)  # year (unused)

            if not ϞᚠΘ(ʂƱ):
                return False

            if not ψϯ𝛀Ϲ(ᴺٝшт, ʂƱ):
                return False

        except Exception:
            return False

        return True

    return λΧλΨὨ(date_string)