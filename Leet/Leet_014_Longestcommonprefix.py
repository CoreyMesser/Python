strs = ['pre', 'prea', 'preab', 'pra', 'prab', 'redid', 'redida', 'redidab']


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # self.str_to_list(strs)
        self.starting_letter(self.str_to_list(strs))

    def str_to_list(self, strs):
        strs_lists = []
        for a_str in strs:
            strs_lists.append(list(a_str))
        return strs_lists

# check the first two letters
    def starting_letter(self, strs_lists):
        strs_check = []
        strs_pref = []
        pre_index = 2
        for list in strs_lists:
            for letter_s in strs_lists:
                pre_fix = letter_s[0: pre_index]
                # strs_check.append(pre_fix)
                if pre_fix in strs_lists:
                    strs_pref.append(letter_s)
            pre_index += 1

if __name__ == '__main__':

    sol = Solution()
    sol.longestCommonPrefix(strs)





