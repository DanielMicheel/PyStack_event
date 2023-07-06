def calcula_total(obj, campo):
    total = 0
    for x in obj:
        total += getattr(x, campo)
    return total