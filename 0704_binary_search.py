class Solution:
    def search(self,numsd,target):
        left=0
        right=len(nums)
        while left<right:
            mid = (left + right) // 2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid
        return -1
nums=[-1,0,3,5,9,12]
target=9
print(Solution().search(nums,target))