class Solution:
    def merge(self,intervals):
        intervals.sort(key=lambda x:x[0])
        res=[]
        i=0
        cur=intervals[0]
        while i+1<len(intervals):
            next=intervals[i+1]
            if cur[1]>=next[0]:
                cur[1]=max(cur[1],next[1])
            else:
                res.append(cur)
                cur=next
            i=i+1
        res.append(cur)

        return res


