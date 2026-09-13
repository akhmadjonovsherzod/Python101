def split(data: str, sep=None, maxsplit=-1):

    if data == "":
        return []

    # -------------------------
    # sep is None
    # -------------------------
    if sep is None:

        # No splitting, only remove leading whitespace
        if maxsplit == 0:
            return [data.lstrip()]

        result = []
        current = ""
        splits = 0
        i = 0

        # Skip leading whitespace
        while i < len(data) and data[i].isspace():
            i += 1

        while i < len(data):

            # Normal character
            if not data[i].isspace():
                current += data[i]
                i += 1
                continue

            # We found whitespace
            if current:
                result.append(current)
                current = ""
                splits += 1

                # maxsplit reached
                if maxsplit != -1 and splits == maxsplit:

                    # Skip whitespace
                    while i < len(data) and data[i].isspace():
                        i += 1

                    # Everything remaining becomes one element
                    if i < len(data):
                        result.append(data[i:])

                    return result

            # Skip consecutive whitespace
            while i < len(data) and data[i].isspace():
                i += 1

        if current:
            result.append(current)

        return result

    # -------------------------
    # sep is provided
    # -------------------------

    if maxsplit == 0:
        return [data]

    result = []
    current = ""
    splits = 0
    i = 0

    while i < len(data):

        if data[i:i + len(sep)] == sep and (
            maxsplit == -1 or splits < maxsplit
        ):
            result.append(current)
            current = ""
            splits += 1
            i += len(sep)

        else:
            current += data[i]
            i += 1

    result.append(current)

    return result

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']