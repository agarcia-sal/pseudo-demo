from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    strong = extensions[0]
    my_val = sum(1 for c in strong if c.isupper()) - sum(1 for c in strong if c.islower())
    for s in extensions:
        val = sum(1 for c in s if c.isupper()) - sum(1 for c in s if c.islower())
        if val > my_val:
            strong = s
            my_val = val
    return f"{class_name}.{strong}"