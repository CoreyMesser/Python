x = 10022011


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_l = list(str(x))

        z = self.forward(x_l=x_l)
        y = self.backwards(x_l=x_l)
        if z == y:
            print('T')
            return True
        else:
            print('F')
            return False


    def forward(self, x_l):
        x_a = []
        for a in x_l:
            x_a.append(a)
        xa = "".join(x_a)
        return xa

    def backwards(self, x_l):
        x_b = []
        for b in x_l[::-1]:
            x_b.append(b)
        xb = "".join(x_b)
        return xb



if __name__ == '__main__':
    sol = Solution()
    sol.isPalindrome(x=x)