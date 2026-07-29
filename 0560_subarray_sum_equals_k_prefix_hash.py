class Solution:
    def subarraySum(self,nums,k):
        #构造前缀和
        pre_sum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            pre_sum[i+1]=pre_sum[i]+nums[i]

        cache={}
        count=0
        for i,item in enumerate(pre_sum):
            other=item-k
            if other in cache:
                count+=cache[other]
            cache[item]=cache.get(item,0)+1
        return count


if __name__=='__main__':
    nums=[1,2,3]
    k=3
    print(Solution().subarraySum(nums,k))