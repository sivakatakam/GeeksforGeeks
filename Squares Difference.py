#User function Template for python3
class Solution:
    def squaresDiff (self, N):
        # code here 
        f = 0
        s = 0
        for i in range(1, N + 1):
            f = f + (i * i)
            s = s + i
        s = s * s
        return  abs(f - s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.squaresDiff(N))
# } Driver Code Ends
