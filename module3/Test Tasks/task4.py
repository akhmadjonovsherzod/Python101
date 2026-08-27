def replacer(s: str) -> str:
    return s.translate(str.maketrans('"\'', '\'"'))
