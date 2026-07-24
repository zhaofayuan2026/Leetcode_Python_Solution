#利用读写指针删除有序数组中的重复项
class Solution:
    def RemoveDuplicates(self,nums):
        read=0
        write=0
        while read<len(nums):
            if nums[read]==nums[write]:
                read+=1
            else:
                write+=1
                nums[write]=nums[read]
        return write+1
nums=[0,0,1,1,1,2,2,3,3,4]
print(Solution().RemoveDuplicates(nums))