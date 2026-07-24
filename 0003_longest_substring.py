class Solution:
    def LengthOfLongestSubstring(self,s):
        left=0
        right=0
        my_set=set()
        max_len=0
        while right<len(s):
            if s[right] in my_set:
                my_set.remove(s[right])
                left+=1
            else:
                my_set.add(s[right])
                max_len=max(max_len,len(my_set))
                right+=1
        return max_len

s='abcabcbb'
print(Solution().LengthOfLongestSubstring(s))