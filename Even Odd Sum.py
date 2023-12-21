#User function Template for python3

class Solution:
    def EvenOddSum(self,N,Arr):
        #code here (return list)
        l = [0, 0]
        for i in range(N):
            if i % 2 == 0:
                l[0] += Arr[i]
            else:
                l[1] += Arr[i]
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        ans=ob.EvenOddSum(N,Arr)
        print(ans[0],end=" ")
        print(ans[1])
# } Driver Code Ends
