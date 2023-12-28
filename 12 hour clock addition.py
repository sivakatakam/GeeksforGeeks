#User function Template for python3

class Solution:
    def clockSum(self, num1, num2):
        # code here
        n = num1 + num2
        while n > 11:
            n = n - 12
        return n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1, num2 = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.clockSum(num1, num2))

# } Driver Code Ends
