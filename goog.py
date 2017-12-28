goog_l = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
goog_az = "abcdefghijklmnopqrstuvwxyz"
goog_za = "zyxwvutsrqponmlkjihgfedcba"

goog_li = list(goog_l)
goog_ly = []

for a_letter in goog_li:
    if a_letter in goog_az:
        in_letter = goog_az.index(a_letter)
        out_letter = goog_za[in_letter]
        goog_ly.append(out_letter)
    else:
        goog_ly.append(a_letter)
goog_le = ("".join(goog_ly))
print(goog_l)
print(goog_le)
