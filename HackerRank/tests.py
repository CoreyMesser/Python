# arr = [1,5,3,4,2,3,6,4,6,9]
# k = 5
# b = '1 2 3 6 5 4 8 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 4 4 3 1 5 6 2'
# array = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
# n = 5
# k = 4
# b = '1 2 3 4 5'
# n = 4
# ar = [3, 1, 2, 3]
# m = '2 4 5 9'
# n = '2 4 11 12'

# al = ['3', '2']
# adl = ['1', '5', '3']
# aset = ['3', '1']
# bset = ['5', '7']

s = 'HackerRank.com presents "Pythonist 2".'
class Solution(object):

    def swap_case(self, s):
        a = s.swapcase()

    # def noidea(self, al, adl, aset, bset):
    #     h = 0
    #     for ala in al:
    #         if ala in aset:
    #             h += 1
    #         elif ala in bset:
    #             h -= 1
    #     for adla in adl:
    #         if adla in aset:
    #             h += 1
    #         elif adla in bset:
    #             h -= 1
    #
    #     print(h)

    # def symdiff(self, m, n):
    #     m, n = set(m.strip().split(' ')), set(n.strip().split(' '))
    #     a = n.symmetric_difference(m)
    #     c = []
    #     for h in a:
    #         c.append(int(h))
    #     d = sorted(c)
    #     for b in d:
    #         print(b)


    # def birthdayCakeCandles(self, n, ar):
    #     a, b = set(ar[:int(n / 2):]), set(ar[:-1:int(n / 2)])
    #     c = a.sy(b)
    #     for d in c:
    #         break
    #     print(ar.count(d))

    # def miniMaxSum(self, arr):
    #     a = len(arr)-1
    #     c = []
    #     while a >= 0:
    #         # b = arr
    #         # c.append(sum(b, a-3))
    #         c.append(arr[a - 4] + arr[a - 3] + arr[a - 2] + arr[a - 1])
    #         a -= 1
    #     c.sort()
    #     print (c[a - 1], c[a - 2])

    # def stripper1():
    #     n = int(input().strip())
    #     a = []
    #     for a_i in range(n):
    #         a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    #         a.append(a_t)
    #     result = diagonalDifference(a)
    #     print(result)


    # def array_left_rotation(self, a, n, k):
    #     c = a.index(n)
    #     d = a[n(c-k)]
    #
    #     pass

    # def leftrot(self):
    #     a = list(map(int, b.strip().split(' ')))
    #     answer = self.array_left_rotation(a, n, k);
    #     print(*answer, sep=' ')

    # def average(self, array):
    #     # your code goes here
    #     i=0
    #     print((sum(set(array)))/(len(set(array))))
    #     # a = set(array)
    #     # b = (sum(a))
    #     # c = (len(a))
    #     # print(b/c)
    #     print(i)

    # def captainsroom(self, k, b):
    #     # k, b = int(input()), (input())
    #     d = set(b.split(" "))
    #     e = []
    #     f = (len(b.split(" ")))/k
    #     h = 0
    #     for a in d:
    #         e.append(int(a)*f)
    #
    #     for g in e:
    #         h = g + h
    #
    #     i = (h-(len(b.split(" "))*f))
    #     j = h/f
    #     print(i)


    # def triangle(self, n):
    #     for i in range(1, n):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    #         print()

            # def moddiv(self, a, b):
    #     e = divmod(a, b)
    #     print(e[0])
    #     print(e[1])
    #     print(e)

    # def joinednumber(self, n):
    #     # n = int(input())
    #     a = 0
    #     z = []
    #     while a < n:
    #         z.append(a)
    #         a += 1
    #
    #     b = int(z)
    #     print(int(b))

    # def oddNumbers(self, l, r):
    #     z = []
    #     while l <= r:
    #         z.append(l)
    #         l += 1
    #
    #     for n in z:
    #         if n % 2 == 0:
    #             pass
    #         else:
    #             print n




    # def findNumber(self, arr, k):
    #     for n in arr:
    #         if n == k:
    #             print('YES')
    #             a = 'YES'
    #             return a

if __name__ == '__main__':
    sol = Solution()
    sol.swap_case(s)
