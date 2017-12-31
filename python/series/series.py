def slices(series, length):
    res = []
    if len(series) < length or length == 0: raise ValueError("Incorrect input")
    for i,v in enumerate(series):
        if len(series) - i < length: break
        res.append(list(map(int,series[i:i+length:1])))
    return res
