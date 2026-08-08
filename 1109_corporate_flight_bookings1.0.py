class Solution:
    def corpFlightBookings(self,bookings,n):
        answer=[0]*n
        for first,last,seats in bookings:
            for i in range(first-1,last):
                answer[i]+=seats

        return answer

if __name__ == '__main__':
    bookings=[[1,2,10],[2,3,20],[2,5,25]]
    n=5
    print(Solution().corpFlightBookings(bookings,n))

