#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        x = []
        for i in range(N):
            if a[i] == key:
                x.append(i)
                break
        for i in range(N - 1, - 1, - 1):
            if a[i] == key:
                x.append(i)
                break
        if len(x) == 0:
            x.append(- 1)
            x.append(- 1)
        return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends
