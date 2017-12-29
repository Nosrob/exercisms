def is_isogram(string):
    tmp = []
    for c in filter(lambda x: x.isalpha(),string.lower()):
        if c in tmp:
            return False
        else:
            tmp.append(c)
    return True
