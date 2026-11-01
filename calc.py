def calc(x, n1, n2):
    if x == "+":
        return n1 + n2
    raise ValueError(f"Unsupported operation: {x}")