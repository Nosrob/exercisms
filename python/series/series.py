def slices(series, length):
    if len(series) < length or length == 0: raise ValueError("Incorrect input")
    return [list(map(int, series[i:i+length:1])) for i in range(len(series) - length + 1)]
