def verify(isbn):
    an = [i for i in filter(lambda x: x.isalnum(),isbn)]
    if len(an) != 10: return False

    n = [int(i) for i in filter(lambda x: x.isdigit(),an[:len(an) - 1])]
    if len(n) != 9: return False

    if isbn[-1].isdigit(): n.append(int(isbn[-1]))
    elif isbn[-1] == 'X': n.append(10)
    else: return False

    return (n[0]*10 + n[1]*9 + n[2]*8 + n[3]*7 + n[4]*6 + n[5]*5 + n[6]*4 + n[7]*3 + n[8]*2 + n[9]) % 11 == 0
