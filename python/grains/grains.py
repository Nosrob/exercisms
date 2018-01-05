def on_square(i):
    if i <= 0 or i >= 65 : raise ValueError("Incorrect input")
    return 1 << i - 1

def total_after(i):
    if i <= 0 or i >= 65 : raise ValueError("Incorrect input")
    return (1 << i) - 1
