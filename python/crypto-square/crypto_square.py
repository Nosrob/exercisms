from math import sqrt, ceil

def encode(plain_text):
    if not plain_text : return ''
    normalized = ''.join(filter(str.isalnum, plain_text.lower()))
    c = int(ceil(sqrt(len(normalized))))
    r = int(ceil(len(normalized) / c))
    return ' '.join([normalized[i::c].ljust(r) for i in range(c)])
