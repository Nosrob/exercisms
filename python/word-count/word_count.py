import re
from collections import Counter

def word_count(phrase):
    return Counter(re.findall('[a-z0-9]+\'[a-z0-9]+|[a-z0-9]+', phrase.lower()))
