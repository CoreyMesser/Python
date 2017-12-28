x = 1534236469

class Solution(object):
    def int_reve(self, x):
        x_r = []
        x_l = list(str(x))
        for y in x_l[::-1]:
            if y == '-':
                x_r.insert(0, y)
            else:
                x_r.append(y)
        z = "".join(x_r)
        z_int = int(z)
        if z_int > 2147483647:
            print('0')
            return 0
        elif z_int < -2147483647:
            print('0')

            return 0

        print(int(z_int))
        return int(z_int)

if __name__ == '__main__':
    sol = Solution()
    sol.int_reve(x=x)
