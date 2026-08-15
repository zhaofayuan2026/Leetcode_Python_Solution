class Solution:
    def firstMissingPositive(self,nums):
        i=1
        set_nums=set(nums)

        while True:
            if i in set_nums:
                i=i+1
            else:
                return i
