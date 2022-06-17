# GCD


def gcf(i, j):
    while j != 0:
        (i, j) = (j, i % j)
    return i


print(gcf(60, 48))