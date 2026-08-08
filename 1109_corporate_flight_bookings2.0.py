#借助差分数组解决本题
class Solution:
    def corpFlightBookings(self,bookings,n):
        diff=[0]*(n+1)
        for first, last, seats in bookings:
            diff[first-1]+=seats
            diff[last]-=seats

        answer=[0]*n
        last_seats=0
        for i in range(n):
            answer[i]=last_seats+diff[i]
            last_seats=answer[i]

        return answer

if __name__ == '__main__':
    bookings=[[1,2,10],[2,3,20],[2,5,25]]
    n=5
    print(Solution().corpFlightBookings(bookings,n))
