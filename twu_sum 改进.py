#借助哈希表
class Solutions:
    def twoSum(self, nums, target):
        cache={}
        for i,item in enumerate(nums):
            cache[item]=i

        for i,item in enumerate(nums):
            other=target-item
            if other in cache and cache[other]!=i:
                return [i,cache[other]]
nums=[5,2,3,4,5,6]
target=8
print(Solutions().twoSum(nums,target))

#再进一步，边记边查
class Solutions:
    def twoSum(self, nums, target):
        cache={}
        for i,item in enumerate(nums):
            other=target-item
            if other in cache:
                return [i,cache[other]]
            cache[item]=i
nums=[5,2,3,4,5,6]
target=8
print(Solutions().twoSum(nums,target))
