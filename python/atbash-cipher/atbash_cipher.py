def atbash_cipher(text):
    return ''.join(chr(2 * ord('a') + 25 - ord(x)) if x.isalpha() else x for x in filter(lambda x: x.isalnum() , text.lower()))

def encode(plain_text):
    ciphered = atbash_cipher(plain_text)
    return ' '.join([ciphered[i:i+5] for i in range(0, len(ciphered), 5)])

def decode(ciphered_text):
    return atbash_cipher(ciphered_text)
