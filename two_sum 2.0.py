#双指针法解找有序两数之和
class Solutions:
    def twoSum(self, numbers, target):
        left=0
        right=len(numbers)-1

        while left!=right:
            sum = numbers[left] + numbers[right]
            if sum==target:
                return [left+1,right+1]
            elif sum>target:
                right-=1
            elif sum<target:
                left+=1


numbers = [2, 3, 4, 7, 11, 15]
target = 9
print(Solutions().twoSum(numbers, target))

