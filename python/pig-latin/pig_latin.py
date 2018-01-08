import string

def translate(text):
    vowels = set(["a","e","i","o","u"])
    consonants = set(string.ascii_lowercase) - vowels
    pig_latin = []

    for word in text.split():
        if word[0] in vowels or word.startswith('yt') or word.startswith('xr'):
            pig_latin.append(word + 'ay')
        elif word.startswith('squ') or word.startswith('sch') or word.startswith('thr'):
            pig_latin.append(word[3:] + word[0:3] + 'ay')
        elif word.startswith('qu') or (word[0] in consonants and (word[1] in consonants - set("y"))):
            pig_latin.append(word[2:] + word[0:2] + 'ay')
        elif (word[0] in consonants):
            pig_latin.append(word[1:] + word[0] + 'ay')
    return ' '.join(pig_latin)
