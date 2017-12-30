def decode(string):
    if len(string) == 0: return string

    number = ""
    result = ""
    cursor = string[0]

    for char in string:
        if char.isdigit():
            number += char
        elif cursor.isdigit():
            result += char * int(number)
            number = ""
        else:
            result += char
        cursor = char
    return result

def encode(string):
    if len(string) == 0: return string

    result = ""
    cursor = string[0]
    counter = 0

    for char in string:
        if char == cursor:
            counter += 1
        else:
            if counter > 1: result += str(counter)
            result += cursor
            counter = 1
        cursor = char
    else:
        if counter > 1: result += str(counter)
        result += cursor
    return result
