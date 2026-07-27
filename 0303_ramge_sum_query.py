class NumArray:
    def __init__(self,nums):
        self.preSum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.preSum[i+1]=self.preSum[i]+nums[i]

    def sumRange(self,left,right):
        return self.preSum[right+1]-self.preSum[left]


if __name__ == '__main__':
    a=NumArray([0,1,2,3,4,5,6])
    print(a.sumRange(0,2))