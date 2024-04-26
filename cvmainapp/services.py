# Helper functions

def years_to_word(years: int, lang: str="ru"):
    word_years = (
        "year" + ("s" if years > 1 else "") if lang == "eng" else
        "лет" if str(years).endswith(
            ("0", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14")
        ) else "год" if str(years).endswith("1") else "года")
    
    return f"{years} {word_years}"
