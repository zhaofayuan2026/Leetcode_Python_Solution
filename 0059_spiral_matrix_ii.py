#利用边界收缩法解决螺旋矩阵
class Solution:
    def generateMatrix(self,n):
        mat=[[0]*n for _ in range(n)]
        top,bottom=0,n-1
        left,right=0,n-1
        count=1
        while count<=n*n:
            for j in range(left,right+1):
                mat[top][j]=count
                count+=1
            top+=1
            for i in range(top,bottom+1):
                mat[i][right]=count
                count+=1
            right-=1
            for j in range(right,left-1,-1):
                mat[bottom][j]=count
                count+=1
            bottom-=1
            for i in range(bottom,top-1,-1):
                mat[i][left]=count
                count+=1
            left+=1
        return mat
print(Solution().generateMatrix(3))