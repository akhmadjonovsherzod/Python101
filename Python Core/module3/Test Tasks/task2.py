def get_fractions(a_b: str, c_b: str) -> str:
    numerator1, denominator1 = a_b.split("/")
    numerator2, denominator2 = c_b.split("/")

    sum_num = int(numerator1) + int(numerator2)

    result = f"{a_b} + {c_b} = {sum_num}/{denominator1}"

    return result