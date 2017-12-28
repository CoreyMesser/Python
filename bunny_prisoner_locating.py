#match bunny prisoners IDs to cell locations
#the bunny prisoners are given numerical IDs starting from the corner, as follows:



#Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.
#example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely

#Write a function answer(x, y) which returns the prisoner ID of the bunny at location (x, y).
#Each value of x and y will be at least 1 and no greater than 100,000.
#Since the prisoner ID can be very large, return your answer as a string representation of the number.

# Test cases
# ==========
#
# Inputs:
#     (int) x = 3
#     (int) y = 2
# Output:
#     (string) "9"
#
# Inputs:
#     (int) x = 5
#     (int) y = 10
# Output:
#     (string) "96"
#
#
# Inputs:
#     (int) x = 3
#     (int) y = 4
# Output:
#     (string) "18"
#
# 8| 29
# 7| 22 30
# 6| 16 23 31
# 5| 11 17 24 32
# 4| 7  12 18 25 33
# 3| 4  8  13 19 26 34
# 2| 2  5  9  14 20 27 35
# 1| 1  3  6  10 15 21 28 36
# Y  -----------------------
#  X 1  2  3  4  5  6   7  8
#def goog_bun(goog_x, goog_y):

# 7 = x1 y4
# 8 = x2 y3
# 14= x4 y2
# 21= x6 y1
#
# CONSTANT 1,1 is ALWAYS 1
#
# x = a + (position of a+1)    ie 3 is located at index 2 + 1 = 6, 15 is located at 5 + 1 = 21,
# y = (position of a+y) + x    ie 18 is located at x3, y4,  x=(1 + (1+2) = 3 + (2+1) = 6), y=(6+3 = 9+4 = 13+5 = 18)

#if you move 4 in any direction that means 4 in the other direction has also been filled with numbers but we have to assume that the whole
#     grid is filled. but we should be able to find any single number assuming the first arg is true
#  4*4 = 16 but the grid is only partially filled, 4 # along x and the same along y, 8 - 1 for the reused number
#
# (x * y) - ()

goog_x = 1
goog_y = 213

goog_xl = goog_x
goog_yl = goog_y
goog_yc = 0
goog_xc = 0

goog_a, goog_b = 1, 0
goog_xa, goog_ya = 0, 0

if goog_x is not 1:
    while goog_xl > 1:
        goog_xl -= 1
        goog_a, goog_b = goog_a, goog_a + goog_b + goog_xc
        goog_xc += 1
    goog_xa = goog_b + goog_x
else:
    goog_xa = 1

if goog_y is not 1:
    while goog_yl > 1:
        goog_yl -= 1
        goog_ya = goog_xa + (goog_x + goog_yc)
        goog_xa = goog_ya
        goog_yc += 1
else:
    goog_ya = goog_xa

print(goog_ya)
