def xo(s: str) -> bool:
    x = o = 0
    for i in s.lower():
        if i == "x":
            x += 1
        elif i == "o":
            o += 1
    return x == o
