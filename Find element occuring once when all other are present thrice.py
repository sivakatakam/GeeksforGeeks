#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here
        c = {}
        for i in arr:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
        for key, value in c.items():
            if value == 1:
                return key


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends
