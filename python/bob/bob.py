def hey(phrase):
    s = "".join(phrase.split())
    if len(s) == 0:
        return "Fine. Be that way!"
    elif s.isupper():
        return "Whoa, chill out!"
    elif s[len(s)-1] == '?':
        return "Sure."
    return "Whatever."
