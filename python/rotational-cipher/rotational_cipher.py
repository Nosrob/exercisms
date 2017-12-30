def rotate(text, key):
    res = ""
    for char in text:
        num = ord(char)
        if char.isupper() and (num + key) > ord('Z'): res += chr(num + key - 26)
        elif char.islower() and (num + key) > ord('z'): res += chr(num + key - 26)
        elif char.isalpha(): res += chr(num + key)
        else: res += char
    return res
