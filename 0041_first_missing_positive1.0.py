class Solution:
    def firstMissingPositive(self,nums):
        i=1
        while True:
            if i in nums:
                i=i+1
            else:
                return i
