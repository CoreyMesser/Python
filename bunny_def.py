def answer(x, y):
    goog_xl = x
    goog_yl = y
    goog_yc = 0
    goog_xc = 0
    goog_a, goog_b = 1, 0
    goog_xa, goog_ya = 0, 0
    if x is not 1:
        while goog_xl > 1:
            goog_xl -= 1
            goog_a, goog_b = goog_a, goog_a + goog_b + goog_xc
            goog_xc += 1
        goog_xa = goog_b + x
    else:
        goog_xa = 1
    if y is not 1:
        while goog_yl > 1:
            goog_yl -= 1
            goog_ya = goog_xa + (x + goog_yc)
            goog_xa = goog_ya
            goog_yc += 1
    else:
        goog_ya = goog_xa
    return goog_ya
