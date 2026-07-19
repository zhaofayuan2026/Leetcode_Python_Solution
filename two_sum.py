class Solutions:
    def twoSum(self,nums,target):
        for i,item in enumerate(nums):
            for j in range (i+1,len(nums)):
                post=nums[j]
                if item+post==target:
                    return [i,j]
nums=[5,2,3,4,5,6]
target=8
print(Solutions().twoSum(nums,target))


