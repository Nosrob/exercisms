def flatten(iterable):
    result = []
    for i in iterable:
        if isinstance(i, (int, str)): result.append(i)
        elif isinstance(i, list): result.extend(flatten(i))
    return result
