#User function Template for python3
class Solution:
    def delAlternate (ob, S):
        # code here 
        s = ''
        for i in range(0, len(S), 2):
            s = s + S[i]
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        
        ob = Solution()
        print(ob.delAlternate(S))
# } Driver Code Ends
