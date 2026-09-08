def union(*args) -> set:

    my_set = set()
    for i in args:
        i = set(i)
        my_set.update(i)

    return my_set


def intersect(*args) -> set:
    my_set = set(args[0])

    for item in args[1:]:
        my_set = my_set.intersection(item)

    return my_set

