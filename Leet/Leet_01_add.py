nums = [3, 2, 3]
target = 6


class Solution(object):
    def twoSum(self, nums, target):
        num_z = []

        for num_a in enumerate(nums):
            num_z.append(num_a)

"".join

# class Solution(object):
#     def twoSum(self, nums, target):
#         num_a = 0
#         num_b = 0
#         num_c = 0
#         num_d = -1
#
#         if len(nums) <= 2:
#             return 0, 1
#
#         for num_a in nums:
#             num_c = num_a + num_b
#             if num_c - target == 0:
#                 num_c = 0
#                 break
#             num_b = num_a
#
#         if num_c != 0:
#             return None
#         elif num_a == num_b:
#             nums_i = []
#             for num_e in nums:
#                 if num_e == num_a:
#                     nums_i.append(num_d)
#                 num_d += 1
#             nums_i.pop(0)
#             num_a = nums_i[0]
#
#             print('elif', nums.index(num_b), num_a)
#             return nums.index(num_b), num_a
#
#         print(nums.index(num_b), nums.index(num_a))
#         return nums.index(num_b), nums.index(num_a)




        # for num_a in nums:
        #     for num_b in nums:
        #         num_c = num_a + num_b
        #         if num_c == target:
        #             print(nums.index(num_a), nums.index(num_b))
        # return nums.index(num_a), nums.index(num_b)



if __name__ == '__main__':
    sol = Solution()
    sol.twoSum(nums=nums, target=target)
