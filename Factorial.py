#User function Template for python3


class Solution:
    def factorial (self, N):
        # code here
        c = 1
        for i in range(1, N + 1):
            c = c * i
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.factorial(N))

# } Driver Code Ends
