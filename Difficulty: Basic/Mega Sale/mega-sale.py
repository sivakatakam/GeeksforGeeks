class Solution:
    def maxProfit(self, m, arr):
        #Your code goes here
        n = []
        for i in arr:
            if i < 0:
                n.append(-i)
        n.sort()
        n.reverse()
        return(sum(n[0 : m]))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxProfit(k, arr))
        print("~")

# } Driver Code Ends