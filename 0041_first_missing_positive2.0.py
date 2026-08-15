#原地哈希表
class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([1,2,3,4,5]))


