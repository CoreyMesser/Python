nums = [1, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9, 9, 9, 9, 10, 10, 11, 12, 13]
# nums = [1]

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        else:
            i, k = 0, len(nums)

            while i < k:
                if nums[i] == nums[i+1]:
                    del nums[i]
                    k -= 1
                else:
                    i += 1

            print(len(nums))
            return len(nums)

if __name__ == '__main__':

    sol = Solution()
    sol.removeDuplicates(nums=nums)
