def c_to_f(celsius):
    return celsius * (9/5) + 32

def describe(celsius):
    if celsius > 30:
        return "hot"
    elif celsius < 15:
        return "cold"
    return "pleasant"
