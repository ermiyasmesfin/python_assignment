# intersect lines
# y=mx +b


def intersect(m1, b1, m2, b2):
    if m1 != m2:
        return 1
    if (m1 == m2) and (b1 == b2):
        return 1
    if (m1 == m2) and (b1 != b2):
        return 0


print(intersect(3, 5, 3, 5))