from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    s_lower = s.lower()

    s_letters = {}
    for i in s_lower:
        if i in s_letters:
            s_letters[i] += 1
        else:
            s_letters[i] = 1
    return s_letters