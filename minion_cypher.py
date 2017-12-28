#goog_l = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
#establish length of input
#loop through input and check the letter against list_az, ensure to check for white spaces, punctuation and special characters
#UPPERCASE AND PUNCTUATION ARE LEFT UNTOUCHED
#check the index of the letter in the list_az
#apply that index to list_za
#apply corresponding letter to cached letter_list
#return final list as a converted sentance

def googly(goog_l):
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
    goog_le =  ("".join(goog_ly))
    return goog_le


while True:
    goog_l = input(">>")
    googly(goog_l)

    # if __name__ == '__main__':
#    pass
#https://www.google.com/foobar/?eid=rXHAWKOxNenm0gLuu7uoDA&usg=AG3vBD11EbGeyOGmU9eTyORT_GSipJ6fdg