def get_longest_word( s: str) -> str:
    list_s = s.strip().split()
    longest = ""
    for i in list_s:
        if len(longest) < len(i):
            longest = i
    return longest