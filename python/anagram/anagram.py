from collections import Counter

def detect_anagrams(word, candidates):
        return [c for c in candidates if c.lower() != word.lower() and Counter(word.lower()) == Counter(c.lower())]
